"""Illustrative field-service toy simulation.

This module is intentionally small and educational. It is not a reproduction
of the paper, uses no paper data, and makes no empirical claim about the
paper's findings. The goal is to make the core trade-off visible:

- flexible technicians can handle emergency and PM jobs;
- PM-focused technicians improve planned maintenance capacity;
- delayed PM can create avoidable emergency pressure.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from math import ceil, exp
import argparse
import random
from statistics import mean


@dataclass(frozen=True)
class SimulationConfig:
    """Parameters for the illustrative model.

    The values are synthetic. They are chosen to be plausible enough for a
    teaching example, not to describe a real field-service organization.
    """

    days: int = 90
    machine_count: int = 220
    technicians: int = 10
    jobs_per_technician_per_day: int = 2
    workload: float = 2.1
    preventive_maintenance_interval: int = 30
    machine_reliability_proxy: float = 0.55
    dedicated_technician_ratio: float = 0.2
    seed: int = 42


@dataclass(frozen=True)
class DayResult:
    day: int
    scheduled_pm: int
    base_emergencies: int
    converted_pm_to_emergency: int
    pm_completed: int
    emergency_completed: int
    pm_backlog: int
    emergency_backlog: int
    utilization: float
    emergency_response_proxy: float
    pm_timeliness_proxy: float
    penalty_like_score: float


@dataclass(frozen=True)
class ScenarioSummary:
    dedicated_technician_ratio: float
    workload: float
    preventive_maintenance_interval: int
    machine_reliability_proxy: float
    avg_emergency_response_proxy: float
    avg_pm_timeliness_proxy: float
    avg_penalty_like_score: float
    avg_utilization: float
    final_pm_backlog: int
    final_emergency_backlog: int


def _poisson(rng: random.Random, average: float) -> int:
    """Sample from a Poisson distribution using only the Python standard lib."""

    if average <= 0:
        return 0

    threshold = exp(-average)
    product = 1.0
    count = 0

    while product > threshold:
        count += 1
        product *= rng.random()

    return count - 1


def _bounded(value: float, low: float, high: float) -> float:
    return max(low, min(high, value))


def _pm_grace_days(config: SimulationConfig) -> int:
    """Allowed PM delay before lateness starts to hurt the proxy metric."""

    return max(2, ceil(config.preventive_maintenance_interval * 0.15))


def _daily_pm_rate(config: SimulationConfig) -> float:
    """Synthetic expected PM jobs per day."""

    interval = max(1, config.preventive_maintenance_interval)
    return config.workload * config.machine_count / interval


def _daily_base_emergency_rate(config: SimulationConfig) -> float:
    """Synthetic expected unavoidable emergency jobs per day."""

    reliability_gap = 1.0 - _bounded(config.machine_reliability_proxy, 0.0, 1.0)
    return config.workload * (0.9 + 7.0 * reliability_gap)


def _pm_conversion_probability(age: int, config: SimulationConfig) -> float:
    """Chance that an overdue PM item becomes an avoidable emergency.

    This is deliberately simple. Lower reliability and longer delay increase
    conversion risk; shorter PM intervals also make lateness more consequential.
    """

    overdue_days = max(0, age - _pm_grace_days(config))
    if overdue_days == 0:
        return 0.0

    reliability_gap = 1.0 - _bounded(config.machine_reliability_proxy, 0.0, 1.0)
    interval_pressure = 30 / max(10, config.preventive_maintenance_interval)
    probability = 0.01 + 0.035 * reliability_gap + 0.004 * overdue_days * interval_pressure
    return _bounded(probability, 0.0, 0.28)


def run_simulation(config: SimulationConfig) -> list[DayResult]:
    """Run the illustrative field-service toy model."""

    rng = random.Random(config.seed)
    dedicated_technicians = round(config.technicians * config.dedicated_technician_ratio)
    dedicated_technicians = max(0, min(config.technicians, dedicated_technicians))
    flexible_technicians = config.technicians - dedicated_technicians

    dedicated_capacity = dedicated_technicians * config.jobs_per_technician_per_day
    flexible_capacity = flexible_technicians * config.jobs_per_technician_per_day
    total_capacity = dedicated_capacity + flexible_capacity

    pm_backlog_ages: list[int] = []
    emergency_backlog = 0
    results: list[DayResult] = []

    for day in range(1, config.days + 1):
        pm_backlog_ages = [age + 1 for age in pm_backlog_ages]

        scheduled_pm = _poisson(rng, _daily_pm_rate(config))
        pm_backlog_ages.extend([0] * scheduled_pm)

        remaining_pm_ages: list[int] = []
        converted_pm_to_emergency = 0
        for age in pm_backlog_ages:
            if rng.random() < _pm_conversion_probability(age, config):
                converted_pm_to_emergency += 1
            else:
                remaining_pm_ages.append(age)
        pm_backlog_ages = remaining_pm_ages

        base_emergencies = _poisson(rng, _daily_base_emergency_rate(config))
        emergency_backlog += base_emergencies + converted_pm_to_emergency
        emergency_demand_before_service = emergency_backlog

        emergency_completed = min(emergency_backlog, flexible_capacity)
        emergency_backlog -= emergency_completed
        remaining_flexible_capacity = flexible_capacity - emergency_completed

        pm_capacity = dedicated_capacity + remaining_flexible_capacity
        pm_backlog_ages.sort(reverse=True)

        pm_completed = min(len(pm_backlog_ages), pm_capacity)
        completed_pm_ages = pm_backlog_ages[:pm_completed]
        pm_backlog_ages = pm_backlog_ages[pm_completed:]

        grace_days = _pm_grace_days(config)
        observed_pm_ages = completed_pm_ages + pm_backlog_ages
        if observed_pm_ages:
            avg_pm_delay = mean(max(0, age - grace_days) for age in observed_pm_ages)
            pm_timeliness_proxy = 1 / (1 + avg_pm_delay)
        else:
            pm_timeliness_proxy = 1.0

        emergency_response_proxy = emergency_demand_before_service / max(1, flexible_capacity)
        utilization = (pm_completed + emergency_completed) / max(1, total_capacity)

        pm_backlog_pressure = len(pm_backlog_ages) / max(1, total_capacity)
        emergency_backlog_pressure = emergency_backlog / max(1, flexible_capacity)
        penalty_like_score = (
            2.2 * emergency_response_proxy
            + 1.6 * (1.0 - pm_timeliness_proxy)
            + 0.35 * pm_backlog_pressure
            + 0.55 * emergency_backlog_pressure
        )

        results.append(
            DayResult(
                day=day,
                scheduled_pm=scheduled_pm,
                base_emergencies=base_emergencies,
                converted_pm_to_emergency=converted_pm_to_emergency,
                pm_completed=pm_completed,
                emergency_completed=emergency_completed,
                pm_backlog=len(pm_backlog_ages),
                emergency_backlog=emergency_backlog,
                utilization=utilization,
                emergency_response_proxy=emergency_response_proxy,
                pm_timeliness_proxy=pm_timeliness_proxy,
                penalty_like_score=penalty_like_score,
            )
        )

    return results


def summarize(results: list[DayResult], config: SimulationConfig) -> ScenarioSummary:
    """Return a compact scenario summary."""

    if not results:
        return ScenarioSummary(
            dedicated_technician_ratio=config.dedicated_technician_ratio,
            workload=config.workload,
            preventive_maintenance_interval=config.preventive_maintenance_interval,
            machine_reliability_proxy=config.machine_reliability_proxy,
            avg_emergency_response_proxy=0.0,
            avg_pm_timeliness_proxy=0.0,
            avg_penalty_like_score=0.0,
            avg_utilization=0.0,
            final_pm_backlog=0,
            final_emergency_backlog=0,
        )

    return ScenarioSummary(
        dedicated_technician_ratio=config.dedicated_technician_ratio,
        workload=config.workload,
        preventive_maintenance_interval=config.preventive_maintenance_interval,
        machine_reliability_proxy=config.machine_reliability_proxy,
        avg_emergency_response_proxy=mean(day.emergency_response_proxy for day in results),
        avg_pm_timeliness_proxy=mean(day.pm_timeliness_proxy for day in results),
        avg_penalty_like_score=mean(day.penalty_like_score for day in results),
        avg_utilization=mean(day.utilization for day in results),
        final_pm_backlog=results[-1].pm_backlog,
        final_emergency_backlog=results[-1].emergency_backlog,
    )


def run_ratio_sweep(
    base_config: SimulationConfig,
    ratios: list[float] | tuple[float, ...] = (0.0, 0.1, 0.2, 0.3, 0.4, 0.5),
) -> list[ScenarioSummary]:
    """Compare dedicated technician ratios under the same synthetic scenario."""

    summaries: list[ScenarioSummary] = []
    for ratio in ratios:
        scenario_config = replace(base_config, dedicated_technician_ratio=ratio)
        summaries.append(summarize(run_simulation(scenario_config), scenario_config))
    return summaries


def print_summary_table(summaries: list[ScenarioSummary]) -> None:
    headers = (
        "dedicated",
        "emergency_proxy",
        "pm_timeliness",
        "penalty_like",
        "utilization",
        "pm_backlog",
        "em_backlog",
    )
    print(" | ".join(headers))
    print(" | ".join("---" for _ in headers))
    for row in summaries:
        print(
            " | ".join(
                [
                    f"{row.dedicated_technician_ratio:.2f}",
                    f"{row.avg_emergency_response_proxy:.2f}",
                    f"{row.avg_pm_timeliness_proxy:.2f}",
                    f"{row.avg_penalty_like_score:.2f}",
                    f"{row.avg_utilization:.2f}",
                    str(row.final_pm_backlog),
                    str(row.final_emergency_backlog),
                ]
            )
        )


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workload", type=float, default=2.1)
    parser.add_argument("--pm-interval", type=int, default=30)
    parser.add_argument("--reliability", type=float, default=0.55)
    parser.add_argument("--days", type=int, default=90)
    parser.add_argument("--technicians", type=int, default=10)
    parser.add_argument("--seed", type=int, default=42)
    return parser


def main() -> None:
    args = build_arg_parser().parse_args()
    config = SimulationConfig(
        days=args.days,
        technicians=args.technicians,
        workload=args.workload,
        preventive_maintenance_interval=args.pm_interval,
        machine_reliability_proxy=args.reliability,
        seed=args.seed,
    )
    print("Illustrative toy simulation - not a reproduction of the paper.")
    print_summary_table(run_ratio_sweep(config))


if __name__ == "__main__":
    main()
