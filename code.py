import json
import time
from datetime import datetime
from typing import Dict, List, Optional
from dataclasses import dataclass
from enum import Enum


class EmergencyType(Enum):
    CHEMICAL_SPILL = "chemical_spill"
    FIRE = "fire"
    MEDICAL_EMERGENCY = "medical_emergency"
    ELECTRICAL_ACCIDENT = "electrical_accident"
    GAS_LEAK = "gas_leak"
    BIOLOGICAL_SPILL = "biological_spill"


@dataclass
class EmergencyStep:
    order: int
    instruction: str
    time_estimate: int  # seconds
    critical: bool = False


class LabSafetyProtocol:
    """Manages lab safety manuals and emergency protocols"""

    def _init_(self):
        self.emergency_protocols = self._load_protocols()
        self.incident_log = []

    def _load_protocols(self) -> Dict[EmergencyType, List[EmergencyStep]]:
        """Load emergency protocols from internal database"""
        return {
            EmergencyType.CHEMICAL_SPILL: [
                EmergencyStep(1, "ALERT: Evacuate immediate area and warn others", 10, True),
                EmergencyStep(2, "Don appropriate PPE (gloves, goggles, lab coat)", 30, True),
                EmergencyStep(3, "Locate spill kit and absorbent materials", 60),
                EmergencyStep(4, "Contain spill boundaries using absorbent booms", 120),
                EmergencyStep(5, "Apply neutralizing agent if appropriate", 90),
                EmergencyStep(6, "Dispose of contaminated materials in chemical waste container", 180),
                EmergencyStep(7, "Contact safety officer at extension 5555", 30, True),
                EmergencyStep(8, "Complete incident report", 300)
            ],
            EmergencyType.FIRE: [
                EmergencyStep(1, "ACTIVATE nearest fire alarm pull station", 5, True),
                EmergencyStep(2, "EVACUATE immediately - do not use elevators", 10, True),
                EmergencyStep(3, "Call emergency services at 555-0123", 15, True),
                EmergencyStep(4, "Use fire extinguisher only if trained and fire is small", 30),
                EmergencyStep(5, "Pass fire extinguisher: Pull pin, Aim base, Squeeze, Sweep", 45),
                EmergencyStep(6, "Close doors/windows behind you to contain fire", 20),
                EmergencyStep(7, "Proceed to designated assembly point", 60, True),
                EmergencyStep(8, "Do not re-enter until cleared by safety personnel", 0, True)
            ],
            EmergencyType.MEDICAL_EMERGENCY: [
                EmergencyStep(1, "ASSESS scene safety - do not put yourself at risk", 10, True),
                EmergencyStep(2, "Call for help - dial 555-0123", 5, True),
                EmergencyStep(3, "Check consciousness - tap and shout", 15),
                EmergencyStep(4, "Provide first aid according to your training level", 60),
                EmergencyStep(5, "Retrieve first aid kit and AED if available", 30),
                EmergencyStep(6, "Do not move victim unless in immediate danger", 5, True),
                EmergencyStep(7, "Stay with victim until help arrives", 0, True)
            ],
            EmergencyType.ELECTRICAL_ACCIDENT: [
                EmergencyStep(1, "DO NOT touch victim if still in contact with electrical source", 5, True),
                EmergencyStep(2, "TURN OFF main power switch immediately", 10, True),
                EmergencyStep(3, "Use non-conductive object (wood broom) to separate victim", 20, True),
                EmergencyStep(4, "Call emergency services at 555-0123", 10, True),
                EmergencyStep(5, "Check breathing and pulse - begin CPR if needed", 30),
                EmergencyStep(6, "Report to safety department with electrical panel location", 60)
            ]
        }

    def get_emergency_protocol(self, emergency_type: EmergencyType) -> List[EmergencyStep]:
        """Retrieve protocol for specific emergency type"""
        return self.emergency_protocols.get(emergency_type, [])

    def run_emergency_response(self, emergency_type: EmergencyType, interactive: bool = True):
        """Executes step-by-step emergency protocol with timing"""

        protocol = self.get_emergency_protocol(emergency_type)

        if not protocol:
            print(f"No protocol found for emergency type: {emergency_type}")
            return

        print(f"\n{'=' * 60}")
        print(f"EMERGENCY RESPONSE: {emergency_type.value.upper().replace('_', ' ')}")
        print(f"Start time: {datetime.now().strftime('%H:%M:%S')}")
        print(f"{'=' * 60}\n")

        # Log incident start
        self.incident_log.append({
            'type': emergency_type.value,
            'start_time': datetime.now(),
            'steps_completed': []
        })

        for step in protocol:
            prefix = "⚠️ CRITICAL" if step.critical else "📋 STEP"
            print(f"{prefix} {step.order}: {step.instruction}")

            if interactive and step.time_estimate > 0:
                response = input(f"✅ Complete step {step.order}? (y/n, or 'skip'): ").lower()

                if response == 'skip':
                    print(f"⚠️ WARNING: Skipped step {step.order} - may affect safety")
                elif response != 'y':
                    print(f"❓ Step {step.order} not completed. Please complete before proceeding.")
                    response = input(f"Continue after completing step {step.order}? (y/n): ").lower()
                    if response != 'y':
                        print("⚠️ Emergency response paused!")
                        break

            # Log completion
            self.incident_log[-1]['steps_completed'].append(step.order)

            if step.time_estimate > 0:
                print(f"⏱️ Estimated time: {step.time_estimate} seconds")
                time.sleep(1)  # Brief pause between steps
            print("-" * 50)

        print(f"\n✅ Emergency protocol completed at {datetime.now().strftime('%H:%M:%S')}")
        print("📝 Please complete incident report form when safe")


class SafetyManualDatabase:
    """Manage lab safety manuals and industrial operating procedures"""

    def _init_(self):
        self.manuals = {}
        self.procedures = {}
        self._initialize_manuals()

    def _initialize_manuals(self):
        """Initialize safety manuals and SOPs"""
        self.manuals = {
            "chemical_safety": {
                "version": "3.2",
                "last_updated": "2024-01-15",
                "sections": ["Storage", "Handling", "Waste Disposal", "Emergency Response"],
                "key_points": [
                    "Always review SDS before handling chemicals",
                    "Wear appropriate PPE at all times",
                    "Never work alone with hazardous materials",
                    "Label all containers properly"
                ]
            },
            "equipment_safety": {
                "version": "2.1",
                "last_updated": "2024-02-01",
                "sections": ["Pre-use Inspection", "Operation", "Maintenance", "Lockout/Tagout"],
                "key_points": [
                    "Complete pre-use checklist",
                    "Know emergency shutdown procedures",
                    "Keep guards in place",
                    "Report malfunction immediately"
                ]
            }
        }

        self.procedures = {
            "ppe_donning": [
                "1. Inspect all PPE for damage",
                "2. Put on gown/coverall",
                "3. Put on mask/respirator",
                "4. Put on goggles/face shield",
                "5. Put on gloves (cover gown cuffs)",
                "6. Verify complete coverage"
            ],
            "waste_disposal": [
                "1. Segregate waste by type",
                "2. Use appropriate container",
                "3. Complete waste tag form",
                "4. Seal container properly",
                "5. Move to designated waste area"
            ]
        }

    def search_procedure(self, keyword: str) -> List[str]:
        """Search procedures by keyword"""
        results = []
        keyword_lower = keyword.lower()

        for proc_name, steps in self.procedures.items():
            if keyword_lower in proc_name or any(keyword_lower in step.lower() for step in steps):
                results.extend([f"\n🔍 Found in '{proc_name}':", *steps])

        return results if results else ["No matching procedures found"]


class SafetyAssistanceSystem:
    """Main interface for lab safety and emergency response"""

    def _init_(self):
        self.protocol = LabSafetyProtocol()
        self.manuals = SafetyManualDatabase()

    def run(self):
        """Main interactive console interface"""
        print("\n" + "=" * 60)
        print("🔬 LAB SAFETY & EMERGENCY RESPONSE SYSTEM 🔬")
        print("=" * 60)

        while True:
            print("\n📋 MAIN MENU:")
            print("1. 🚨 Emergency Protocol (Step-by-Step)")
            print("2. 📚 View Safety Manuals")
            print("3. 🔍 Search Operating Procedures")
            print("4. 📊 View Recent Incidents")
            print("5. 🧪 Quick Chemical Spill Guide")
            print("6. 🔥 Quick Fire Response")
            print("7. ❌ Exit")

            choice = input("\nSelect option (1-7): ").strip()

            if choice == '1':
                self._emergency_mode()
            elif choice == '2':
                self._view_manuals()
            elif choice == '3':
                self._search_procedures()
            elif choice == '4':
                self._view_incidents()
            elif choice == '5':
                self.protocol.run_emergency_response(EmergencyType.CHEMICAL_SPILL)
            elif choice == '6':
                self.protocol.run_emergency_response(EmergencyType.FIRE)
            elif choice == '7':
                print("\n✅ Stay safe! Remember: Safety first, always.")
                break
            else:
                print("❌ Invalid choice. Please select 1-7.")

    def _emergency_mode(self):
        """Handle emergency protocol selection"""
        print("\n🚨 SELECT EMERGENCY TYPE:")
        for i, emergency in enumerate(EmergencyType, 1):
            print(f"{i}. {emergency.value.replace('_', ' ').title()}")

        try:
            choice = int(input("\nEnter number: ")) - 1
            emergency_list = list(EmergencyType)
            if 0 <= choice < len(emergency_list):
                self.protocol.run_emergency_response(emergency_list[choice])
            else:
                print("❌ Invalid selection")
        except ValueError:
            print("❌ Please enter a valid number")

    def _view_manuals(self):
        """Display safety manual sections"""
        print("\n📚 SAFETY MANUALS:")
        for title, content in self.manuals.manuals.items():
            print(f"\n📖 {title.upper().replace('_', ' ')}")
            print(f"   Version: {content['version']} | Updated: {content['last_updated']}")
            print(f"   Sections: {', '.join(content['sections'])}")
            print("   Key Points:")
            for point in content['key_points']:
                print(f"     • {point}")

    def _search_procedures(self):
        """Search for specific procedures"""
        keyword = input("\n🔍 Enter search term (e.g., 'ppe', 'waste'): ").strip()
        results = self.manuals.search_procedure(keyword)
        print("\n" + "\n".join(results))

    def _view_incidents(self):
        """Display recent incident log"""
        if not self.protocol.incident_log:
            print("\n📊 No incidents logged in this session")
        else:
            print(f"\n📊 INCIDENT LOG ({len(self.protocol.incident_log)} entries):")
            for i, incident in enumerate(self.protocol.incident_log[-5:], 1):
                print(f"\n{i}. Type: {incident['type']}")
                print(f"   Time: {incident['start_time'].strftime('%Y-%m-%d %H:%M:%S')}")
                print(f"   Steps completed: {incident['steps_completed']}")


# Run the system
if __name__ == "_main_":
    system = SafetyAssistanceSystem()
    system.run()
