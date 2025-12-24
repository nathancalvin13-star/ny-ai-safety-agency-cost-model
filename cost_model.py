"""
NY Frontier AI Safety Agency Cost Model

This model estimates the annual operating costs for a hypothetical New York State
regulatory agency focused on frontier AI safety risks.

Based on analysis of comparable regulatory agencies:
- NY Department of Financial Services: 1,390 staff, $360M budget
- UK AI Safety Institute: 100+ technical staff, £66M (~$85M USD) budget
- NIST AI Safety Institute: ~$10M initial budget
- California DTSC: ~1,000 staff, ~$196M budget
"""

from dataclasses import dataclass
from typing import Dict, List
import json


@dataclass
class StaffingCategory:
    """Represents a category of staff positions"""
    title: str
    count: int
    avg_salary: float
    description: str

    @property
    def total_cost(self) -> float:
        """Total personnel cost including benefits (30% overhead)"""
        return self.count * self.avg_salary * 1.30


@dataclass
class OperationalCost:
    """Represents an operational expense category"""
    category: str
    annual_cost: float
    description: str


class AIRegulatoryAgencyCostModel:
    """
    Cost model for a NY State Frontier AI Safety Regulatory Agency

    The model covers three scenarios:
    1. Minimal: Small focused team (~50 staff)
    2. Moderate: Medium-sized agency (~150 staff)
    3. Comprehensive: Full-service regulatory body (~300 staff)
    """

    # Salary data based on NY state government compensation
    # Sources: NY OER salary schedules, SeeThroughNY data
    SALARY_RANGES = {
        'executive_leadership': 175000,  # Commissioner, Deputy Commissioners
        'senior_technical': 145000,      # Senior AI Safety Researchers, Principal Engineers
        'technical_staff': 110000,       # AI Safety Researchers, ML Engineers, Evaluators
        'policy_legal': 115000,          # Policy Analysts, Legal Counsel
        'compliance_enforcement': 95000, # Compliance Officers, Enforcement Staff
        'operations_admin': 70000,       # Administrative, HR, Finance, IT
        'junior_technical': 85000,       # Junior Researchers, Analysts
    }

    def __init__(self, scenario: str = 'moderate'):
        """
        Initialize the cost model

        Args:
            scenario: 'minimal', 'moderate', or 'comprehensive'
        """
        self.scenario = scenario
        self.staffing = self._calculate_staffing()
        self.operational_costs = self._calculate_operational_costs()

    def _calculate_staffing(self) -> List[StaffingCategory]:
        """Calculate staffing needs based on scenario"""

        if self.scenario == 'minimal':
            # Small focused team - basic model evaluation and oversight
            return [
                StaffingCategory(
                    'Executive Leadership',
                    3,
                    self.SALARY_RANGES['executive_leadership'],
                    'Commissioner, Deputy Commissioner, Chief of Staff'
                ),
                StaffingCategory(
                    'Senior Technical Staff',
                    8,
                    self.SALARY_RANGES['senior_technical'],
                    'Senior AI Safety Researchers, Principal ML Engineers'
                ),
                StaffingCategory(
                    'Technical Staff',
                    20,
                    self.SALARY_RANGES['technical_staff'],
                    'AI Safety Researchers, ML Engineers, Model Evaluators'
                ),
                StaffingCategory(
                    'Policy & Legal',
                    8,
                    self.SALARY_RANGES['policy_legal'],
                    'Policy Analysts, Legal Counsel, Regulatory Affairs'
                ),
                StaffingCategory(
                    'Compliance & Enforcement',
                    6,
                    self.SALARY_RANGES['compliance_enforcement'],
                    'Compliance Officers, Enforcement Investigators'
                ),
                StaffingCategory(
                    'Operations & Administration',
                    5,
                    self.SALARY_RANGES['operations_admin'],
                    'Administrative Support, HR, Finance, IT'
                ),
            ]

        elif self.scenario == 'moderate':
            # Medium agency - comprehensive evaluation, compliance, enforcement
            return [
                StaffingCategory(
                    'Executive Leadership',
                    5,
                    self.SALARY_RANGES['executive_leadership'],
                    'Commissioner, 2 Deputy Commissioners, Chief of Staff, Strategic Advisor'
                ),
                StaffingCategory(
                    'Senior Technical Staff',
                    20,
                    self.SALARY_RANGES['senior_technical'],
                    'Senior AI Safety Researchers, Principal Engineers, Technical Directors'
                ),
                StaffingCategory(
                    'Technical Staff',
                    60,
                    self.SALARY_RANGES['technical_staff'],
                    'AI Safety Researchers, ML Engineers, Model Evaluators, Security Analysts'
                ),
                StaffingCategory(
                    'Junior Technical Staff',
                    20,
                    self.SALARY_RANGES['junior_technical'],
                    'Junior Researchers, Technical Analysts, Research Associates'
                ),
                StaffingCategory(
                    'Policy & Legal',
                    20,
                    self.SALARY_RANGES['policy_legal'],
                    'Policy Analysts, Legal Counsel, Regulatory Affairs, Interagency Liaisons'
                ),
                StaffingCategory(
                    'Compliance & Enforcement',
                    15,
                    self.SALARY_RANGES['compliance_enforcement'],
                    'Compliance Officers, Enforcement Investigators, Audit Coordinators'
                ),
                StaffingCategory(
                    'Operations & Administration',
                    10,
                    self.SALARY_RANGES['operations_admin'],
                    'Administrative Support, HR, Finance, IT, Communications'
                ),
            ]

        else:  # comprehensive
            # Large full-service agency - proactive monitoring, research, international coordination
            return [
                StaffingCategory(
                    'Executive Leadership',
                    8,
                    self.SALARY_RANGES['executive_leadership'],
                    'Commissioner, 3 Deputy Commissioners, Chief of Staff, Strategic Advisors, Division Directors'
                ),
                StaffingCategory(
                    'Senior Technical Staff',
                    40,
                    self.SALARY_RANGES['senior_technical'],
                    'Senior Researchers, Principal Engineers, Technical Directors, Research Leads'
                ),
                StaffingCategory(
                    'Technical Staff',
                    140,
                    self.SALARY_RANGES['technical_staff'],
                    'AI Safety Researchers, ML Engineers, Evaluators, Security Analysts, Red Team'
                ),
                StaffingCategory(
                    'Junior Technical Staff',
                    40,
                    self.SALARY_RANGES['junior_technical'],
                    'Junior Researchers, Technical Analysts, Research Associates'
                ),
                StaffingCategory(
                    'Policy & Legal',
                    35,
                    self.SALARY_RANGES['policy_legal'],
                    'Policy Analysts, Legal Counsel, Regulatory Affairs, International Coordinators'
                ),
                StaffingCategory(
                    'Compliance & Enforcement',
                    25,
                    self.SALARY_RANGES['compliance_enforcement'],
                    'Compliance Officers, Enforcement Investigators, Audit Team, Field Inspectors'
                ),
                StaffingCategory(
                    'Operations & Administration',
                    20,
                    self.SALARY_RANGES['operations_admin'],
                    'Administrative Support, HR, Finance, IT, Communications, Facilities'
                ),
            ]

    def _calculate_operational_costs(self) -> List[OperationalCost]:
        """Calculate operational costs based on scenario and staffing"""

        total_staff = sum(cat.count for cat in self.staffing)

        # Scale factors for different scenarios
        if self.scenario == 'minimal':
            compute_scale = 1.0
            facility_scale = 0.8
            contract_scale = 0.7
        elif self.scenario == 'moderate':
            compute_scale = 2.0
            facility_scale = 1.0
            contract_scale = 1.0
        else:  # comprehensive
            compute_scale = 4.0
            facility_scale = 1.2
            contract_scale = 1.5

        return [
            OperationalCost(
                'Compute Infrastructure & Cloud Services',
                8_000_000 * compute_scale,
                'GPU clusters for model evaluation, cloud services, data storage'
            ),
            OperationalCost(
                'Facilities & Real Estate',
                total_staff * 12_000 * facility_scale,
                'Office space, security, utilities (avg $12k/employee annually in NYC)'
            ),
            OperationalCost(
                'Technology & Software',
                total_staff * 8_000,
                'Software licenses, development tools, security tools, collaboration platforms'
            ),
            OperationalCost(
                'External Research & Contracts',
                5_000_000 * contract_scale,
                'University partnerships, consulting, third-party audits, expert reviews'
            ),
            OperationalCost(
                'Training & Professional Development',
                total_staff * 5_000,
                'Technical training, conferences, certifications, continuing education'
            ),
            OperationalCost(
                'Travel & Outreach',
                1_000_000 * contract_scale,
                'Industry engagement, international coordination, conferences, site visits'
            ),
            OperationalCost(
                'Legal & Compliance',
                800_000 * contract_scale,
                'External legal counsel, compliance tools, regulatory filings'
            ),
            OperationalCost(
                'Communications & Public Affairs',
                500_000 * facility_scale,
                'Public education, stakeholder engagement, reporting, publications'
            ),
            OperationalCost(
                'Emergency Response & Incident Management',
                1_500_000 * compute_scale,
                'Rapid response capabilities, incident investigation, crisis management'
            ),
            OperationalCost(
                'Administrative Overhead',
                500_000 * facility_scale,
                'General supplies, equipment, miscellaneous operational expenses'
            ),
        ]

    @property
    def total_personnel_cost(self) -> float:
        """Total personnel costs including benefits"""
        return sum(cat.total_cost for cat in self.staffing)

    @property
    def total_operational_cost(self) -> float:
        """Total operational costs"""
        return sum(cost.annual_cost for cost in self.operational_costs)

    @property
    def total_annual_cost(self) -> float:
        """Total annual budget requirement"""
        return self.total_personnel_cost + self.total_operational_cost

    @property
    def total_staff_count(self) -> int:
        """Total number of staff"""
        return sum(cat.count for cat in self.staffing)

    @property
    def cost_per_employee(self) -> float:
        """Average cost per employee (fully loaded)"""
        return self.total_annual_cost / self.total_staff_count

    def generate_summary(self) -> Dict:
        """Generate a comprehensive summary of the cost model"""
        return {
            'scenario': self.scenario.title(),
            'total_staff': self.total_staff_count,
            'total_annual_budget': self.total_annual_cost,
            'personnel_costs': self.total_personnel_cost,
            'operational_costs': self.total_operational_cost,
            'cost_per_employee': self.cost_per_employee,
            'staffing_breakdown': [
                {
                    'category': cat.title,
                    'count': cat.count,
                    'avg_salary': cat.avg_salary,
                    'total_cost': cat.total_cost,
                    'description': cat.description
                }
                for cat in self.staffing
            ],
            'operational_breakdown': [
                {
                    'category': cost.category,
                    'annual_cost': cost.annual_cost,
                    'description': cost.description
                }
                for cost in self.operational_costs
            ]
        }

    def print_summary(self):
        """Print a formatted summary to console"""
        print(f"\n{'='*80}")
        print(f"NY FRONTIER AI SAFETY AGENCY - {self.scenario.upper()} SCENARIO")
        print(f"{'='*80}\n")

        print(f"TOTAL ANNUAL BUDGET: ${self.total_annual_cost:,.0f}")
        print(f"Total Staff: {self.total_staff_count}")
        print(f"Cost per Employee (fully loaded): ${self.cost_per_employee:,.0f}")
        print()

        print(f"PERSONNEL COSTS: ${self.total_personnel_cost:,.0f} ({self.total_personnel_cost/self.total_annual_cost*100:.1f}%)")
        print(f"{'-'*80}")
        for cat in self.staffing:
            pct = cat.total_cost / self.total_annual_cost * 100
            print(f"  {cat.title:40} {cat.count:3} staff  ${cat.total_cost:>12,.0f}  ({pct:4.1f}%)")
        print()

        print(f"OPERATIONAL COSTS: ${self.total_operational_cost:,.0f} ({self.total_operational_cost/self.total_annual_cost*100:.1f}%)")
        print(f"{'-'*80}")
        for cost in self.operational_costs:
            pct = cost.annual_cost / self.total_annual_cost * 100
            print(f"  {cost.category:40} ${cost.annual_cost:>12,.0f}  ({pct:4.1f}%)")
        print(f"\n{'='*80}\n")


def compare_scenarios():
    """Compare all three scenarios side by side"""
    scenarios = ['minimal', 'moderate', 'comprehensive']
    models = {s: AIRegulatoryAgencyCostModel(s) for s in scenarios}

    print(f"\n{'='*80}")
    print("SCENARIO COMPARISON")
    print(f"{'='*80}\n")

    print(f"{'Metric':<30} {'Minimal':>15} {'Moderate':>15} {'Comprehensive':>15}")
    print(f"{'-'*80}")
    print(f"{'Total Staff':<30} {models['minimal'].total_staff_count:>15,} {models['moderate'].total_staff_count:>15,} {models['comprehensive'].total_staff_count:>15,}")
    print(f"{'Annual Budget':<30} ${models['minimal'].total_annual_cost:>14,.0f} ${models['moderate'].total_annual_cost:>14,.0f} ${models['comprehensive'].total_annual_cost:>14,.0f}")
    print(f"{'Personnel Costs':<30} ${models['minimal'].total_personnel_cost:>14,.0f} ${models['moderate'].total_personnel_cost:>14,.0f} ${models['comprehensive'].total_personnel_cost:>14,.0f}")
    print(f"{'Operational Costs':<30} ${models['minimal'].total_operational_cost:>14,.0f} ${models['moderate'].total_operational_cost:>14,.0f} ${models['comprehensive'].total_operational_cost:>14,.0f}")
    print(f"{'Cost per Employee':<30} ${models['minimal'].cost_per_employee:>14,.0f} ${models['moderate'].cost_per_employee:>14,.0f} ${models['comprehensive'].cost_per_employee:>14,.0f}")
    print(f"\n{'='*80}\n")

    return models


def export_to_json(filename: str = 'cost_analysis.json'):
    """Export all scenarios to JSON for web interface"""
    scenarios = ['minimal', 'moderate', 'comprehensive']
    data = {
        scenario: AIRegulatoryAgencyCostModel(scenario).generate_summary()
        for scenario in scenarios
    }

    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"Cost analysis exported to {filename}")


if __name__ == '__main__':
    # Print all scenarios
    for scenario in ['minimal', 'moderate', 'comprehensive']:
        model = AIRegulatoryAgencyCostModel(scenario)
        model.print_summary()

    # Compare scenarios
    compare_scenarios()

    # Export to JSON
    export_to_json()
