#!/usr/bin/env python3
"""
Grand Slam Offer Worksheet Generator

An interactive tool for building offers using Alex Hormozi's $100M Offers methodology.
Walks through all 5 steps and generates a complete offer document.

Usage:
    python offer_worksheet_generator.py [--output filename.md]
"""

import argparse
from datetime import datetime
from typing import List, Dict, Optional


class OfferWorksheet:
    """Interactive Grand Slam Offer builder."""
    
    def __init__(self):
        self.data = {
            "avatar": "",
            "dream_outcome": "",
            "problems": [],
            "solutions": [],
            "delivery_vehicles": [],
            "stack": [],
            "bonuses": [],
            "guarantee": {},
            "scarcity": "",
            "urgency": "",
            "name": "",
            "price": "",
            "total_value": 0
        }
        self.problem_categories = ["Likelihood", "Time", "Effort", "Sacrifice"]
    
    def clear_screen(self):
        """Print separator for clarity."""
        print("\n" + "=" * 60 + "\n")
    
    def get_input(self, prompt: str, required: bool = True) -> str:
        """Get user input with optional requirement."""
        while True:
            response = input(f"{prompt}: ").strip()
            if response or not required:
                return response
            print("  → This field is required. Please enter a value.")
    
    def get_multiline(self, prompt: str) -> List[str]:
        """Get multiple lines of input until empty line."""
        print(f"{prompt}")
        print("  (Enter each item on a new line. Empty line to finish)")
        items = []
        while True:
            item = input("  → ").strip()
            if not item:
                break
            items.append(item)
        return items
    
    def get_choice(self, prompt: str, options: List[str]) -> str:
        """Get selection from options."""
        print(f"\n{prompt}")
        for i, opt in enumerate(options, 1):
            print(f"  {i}. {opt}")
        while True:
            try:
                choice = int(input("Select number: "))
                if 1 <= choice <= len(options):
                    return options[choice - 1]
            except ValueError:
                pass
            print(f"  → Please enter a number 1-{len(options)}")
    
    def run_step_1_dream_outcome(self):
        """Step 1: Define avatar and dream outcome."""
        self.clear_screen()
        print("STEP 1: DREAM OUTCOME")
        print("-" * 40)
        print("Define WHO you're helping and WHAT transformation they want.")
        print()
        
        self.data["avatar"] = self.get_input(
            "Who is your ideal customer? (be specific - e.g., 'busy moms over 40')"
        )
        
        print()
        print("What is their dream outcome? Not your process - their END RESULT.")
        print("Frame it as specific, visceral, and status-enhancing.")
        print("Example: 'Lose 20lbs in 6 weeks and have friends ask what your secret is'")
        print()
        
        self.data["dream_outcome"] = self.get_input(
            "Dream outcome"
        )
        
        print()
        print(f"✓ Avatar: {self.data['avatar']}")
        print(f"✓ Dream Outcome: {self.data['dream_outcome']}")
    
    def run_step_2_problems(self):
        """Step 2: List all problems."""
        self.clear_screen()
        print("STEP 2: LIST ALL PROBLEMS")
        print("-" * 40)
        print("Every obstacle between your prospect and their dream = value opportunity.")
        print("List as many as you can - more problems = more value to create.")
        print()
        
        # Get required actions
        print("First, list every ACTION they must take to achieve the dream outcome:")
        actions = self.get_multiline("Actions required")
        
        if not actions:
            actions = ["Complete the program"]  # Default
        
        # For each action, get problems in each category
        for action in actions:
            self.clear_screen()
            print(f"ACTION: {action}")
            print("-" * 40)
            print("List problems in each category (or press Enter to skip):")
            
            for category in self.problem_categories:
                print(f"\n{category.upper()} problems:")
                if category == "Likelihood":
                    print("  (Why won't this work for them specifically?)")
                elif category == "Time":
                    print("  (Why will this take too long?)")
                elif category == "Effort":
                    print("  (Why is this too hard/confusing?)")
                elif category == "Sacrifice":
                    print("  (What must they give up?)")
                
                problems = self.get_multiline(f"  {category} problems for '{action}'")
                for p in problems:
                    self.data["problems"].append({
                        "action": action,
                        "category": category,
                        "problem": p
                    })
        
        print()
        print(f"✓ Total problems identified: {len(self.data['problems'])}")
        print(f"  Each problem is an opportunity to create value in your offer.")
    
    def run_step_3_solutions(self):
        """Step 3: Convert problems to solutions."""
        self.clear_screen()
        print("STEP 3: TURN PROBLEMS INTO SOLUTIONS")
        print("-" * 40)
        print("Convert each problem to a 'How to...' statement.")
        print()
        
        for i, prob in enumerate(self.data["problems"], 1):
            print(f"\nProblem {i}/{len(self.data['problems'])}:")
            print(f"  '{prob['problem']}'")
            
            # Auto-suggest conversion
            suggestion = f"How to overcome {prob['problem'].lower()}"
            response = input(f"  Solution (Enter for suggestion): ").strip()
            
            if not response:
                response = suggestion
            
            self.data["solutions"].append({
                "problem": prob["problem"],
                "solution": response,
                "category": prob["category"]
            })
        
        print()
        print(f"✓ {len(self.data['solutions'])} solutions created")
    
    def run_step_4_delivery(self):
        """Step 4: Create delivery vehicles using Delivery Cube."""
        self.clear_screen()
        print("STEP 4: CREATE DELIVERY VEHICLES")
        print("-" * 40)
        print("Decide HOW you'll deliver each solution.")
        print()
        
        # Group solutions by category for efficiency
        categories = {}
        for sol in self.data["solutions"]:
            cat = sol["category"]
            if cat not in categories:
                categories[cat] = []
            categories[cat].append(sol)
        
        print("For efficiency, we'll create delivery vehicles by category.")
        print("You can use the same vehicle for multiple solutions.\n")
        
        attention_levels = ["1-on-1", "Small Group", "One-to-Many"]
        effort_levels = ["Done-For-You (DFY)", "Done-With-You (DWY)", "Do-It-Yourself (DIY)"]
        
        for category, solutions in categories.items():
            self.clear_screen()
            print(f"CATEGORY: {category.upper()}")
            print(f"Solutions in this category: {len(solutions)}")
            print()
            
            for sol in solutions[:3]:  # Show first 3 as examples
                print(f"  • {sol['solution']}")
            if len(solutions) > 3:
                print(f"  ... and {len(solutions) - 3} more")
            
            print()
            vehicle_name = self.get_input(
                f"What will you create to solve these? (e.g., 'Grocery Shopping Guide')"
            )
            
            attention = self.get_choice("Attention level:", attention_levels)
            effort = self.get_choice("Effort level:", effort_levels)
            
            value = self.get_input("Estimated value ($)", required=False) or "TBD"
            
            self.data["delivery_vehicles"].append({
                "name": vehicle_name,
                "category": category,
                "attention": attention,
                "effort": effort,
                "value": value,
                "solves_count": len(solutions)
            })
        
        print()
        print(f"✓ {len(self.data['delivery_vehicles'])} delivery vehicles created")
    
    def run_step_5_trim_and_stack(self):
        """Step 5: Trim low-value, stack high-value."""
        self.clear_screen()
        print("STEP 5: TRIM & STACK")
        print("-" * 40)
        print("Review your delivery vehicles. Keep high-value, remove low-value.")
        print()
        
        kept = []
        total_value = 0
        
        for vehicle in self.data["delivery_vehicles"]:
            print(f"\n{vehicle['name']}")
            print(f"  Attention: {vehicle['attention']}")
            print(f"  Effort: {vehicle['effort']}")
            print(f"  Solves: {vehicle['solves_count']} problems")
            print(f"  Value: ${vehicle['value']}")
            
            keep = input("  Keep this? (Y/n): ").strip().lower()
            if keep != 'n':
                # Get proper value
                if vehicle['value'] == 'TBD':
                    val = self.get_input("  Assign dollar value", required=False) or "500"
                else:
                    val = vehicle['value']
                
                try:
                    value_int = int(val.replace('$', '').replace(',', ''))
                except:
                    value_int = 500
                
                vehicle['value'] = value_int
                total_value += value_int
                kept.append(vehicle)
        
        self.data["stack"] = kept
        self.data["total_value"] = total_value
        
        print()
        print(f"✓ {len(kept)} items in final stack")
        print(f"✓ Total value: ${total_value:,}")
    
    def run_bonuses(self):
        """Add bonuses."""
        self.clear_screen()
        print("BONUSES")
        print("-" * 40)
        print("Add bonuses to expand price-to-value discrepancy.")
        print("Bonuses should address specific objections or solve 'next' problems.")
        print()
        
        while True:
            add = input("Add a bonus? (y/N): ").strip().lower()
            if add != 'y':
                break
            
            name = self.get_input("Bonus name (with benefit)")
            description = self.get_input("One-line description")
            value = self.get_input("Dollar value")
            
            try:
                value_int = int(value.replace('$', '').replace(',', ''))
            except:
                value_int = 500
            
            self.data["bonuses"].append({
                "name": name,
                "description": description,
                "value": value_int
            })
            self.data["total_value"] += value_int
            
            print(f"  ✓ Added: {name} (${value_int})")
        
        print()
        print(f"✓ {len(self.data['bonuses'])} bonuses added")
        print(f"✓ New total value: ${self.data['total_value']:,}")
    
    def run_guarantee(self):
        """Configure guarantee."""
        self.clear_screen()
        print("GUARANTEE")
        print("-" * 40)
        
        guarantee_types = [
            "Unconditional (No questions asked refund)",
            "Conditional (Refund if they do X and don't get Y)",
            "Service (Keep working until they succeed)",
            "Anti-Guarantee (All sales final)",
            "Performance (Pay only for results)"
        ]
        
        gtype = self.get_choice("Guarantee type:", guarantee_types)
        
        if "Conditional" in gtype:
            conditions = self.get_input("What must they do to qualify?")
            result = self.get_input("What result do you guarantee?")
            self.data["guarantee"] = {
                "type": "Conditional",
                "conditions": conditions,
                "result": result
            }
        elif "Service" in gtype:
            result = self.get_input("What result will you keep working until they achieve?")
            self.data["guarantee"] = {
                "type": "Service",
                "result": result
            }
        else:
            self.data["guarantee"] = {"type": gtype.split(" ")[0]}
        
        name = self.get_input("Give your guarantee a name (optional)", required=False)
        if name:
            self.data["guarantee"]["name"] = name
        
        print()
        print(f"✓ Guarantee configured: {gtype.split(' ')[0]}")
    
    def run_scarcity_urgency(self):
        """Configure scarcity and urgency."""
        self.clear_screen()
        print("SCARCITY & URGENCY")
        print("-" * 40)
        
        scarcity_options = [
            "None",
            "Limited spots (X clients max)",
            "Limited per time period (X per week/month)",
            "Cohort-based (X per class)",
            "Never available again"
        ]
        
        urgency_options = [
            "None",
            "Rolling cohorts (starts Monday)",
            "Seasonal (ends [date])",
            "Pricing deadline (price goes up)",
            "Bonus deadline (bonuses expire)"
        ]
        
        scarcity = self.get_choice("Scarcity type:", scarcity_options)
        if scarcity != "None":
            detail = self.get_input("Specifics (e.g., '5 spots', 'Jan 31')")
            self.data["scarcity"] = f"{scarcity}: {detail}"
        
        urgency = self.get_choice("Urgency type:", urgency_options)
        if urgency != "None":
            detail = self.get_input("Specifics (e.g., 'Monday', 'Feb 28')")
            self.data["urgency"] = f"{urgency}: {detail}"
        
        print()
        print(f"✓ Scarcity: {self.data['scarcity'] or 'None'}")
        print(f"✓ Urgency: {self.data['urgency'] or 'None'}")
    
    def run_naming(self):
        """Name the offer using M.A.G.I.C. formula."""
        self.clear_screen()
        print("NAMING (M.A.G.I.C. Formula)")
        print("-" * 40)
        print("M - Magnet (reason why): Free, 88% Off, Spring, Grand Opening")
        print("A - Avatar: Who it's for")
        print("G - Goal: The outcome")
        print("I - Interval: Timeframe")
        print("C - Container: Challenge, Blueprint, System, etc.")
        print()
        
        m = self.get_input("M - Magnet/Reason Why (optional)", required=False)
        a = self.get_input(f"A - Avatar (suggested: {self.data['avatar']})", required=False) or self.data['avatar']
        g = self.get_input("G - Goal (the outcome)")
        i = self.get_input("I - Interval (e.g., 6-Week, 90-Day)", required=False)
        c = self.get_input("C - Container (e.g., Challenge, Blueprint, System)")
        
        # Build name
        parts = [p for p in [m, a, g, i, c] if p]
        suggested_name = " ".join(parts)
        
        print()
        print(f"Suggested name: {suggested_name}")
        custom = self.get_input("Use this or enter custom name", required=False)
        
        self.data["name"] = custom if custom else suggested_name
        
        print()
        print(f"✓ Offer name: {self.data['name']}")
    
    def run_pricing(self):
        """Set price."""
        self.clear_screen()
        print("PRICING")
        print("-" * 40)
        print(f"Total perceived value: ${self.data['total_value']:,}")
        print(f"Recommended price range: ${self.data['total_value']//10:,} - ${self.data['total_value']//5:,}")
        print("(5-10x value-to-price ratio)")
        print()
        
        self.data["price"] = self.get_input("Your price")
        
        try:
            price_int = int(self.data['price'].replace('$', '').replace(',', ''))
            ratio = self.data['total_value'] / price_int
            print(f"✓ Value-to-price ratio: {ratio:.1f}x")
        except:
            pass
    
    def generate_output(self) -> str:
        """Generate markdown output."""
        output = []
        output.append(f"# {self.data['name']}")
        output.append(f"\n*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}*\n")
        
        output.append("---\n")
        output.append("## Overview\n")
        output.append(f"**Avatar:** {self.data['avatar']}\n")
        output.append(f"**Dream Outcome:** {self.data['dream_outcome']}\n")
        output.append(f"**Price:** {self.data['price']}\n")
        output.append(f"**Total Value:** ${self.data['total_value']:,}\n")
        
        output.append("\n---\n")
        output.append("## The Offer Stack\n")
        
        output.append("### Core Components\n")
        for item in self.data["stack"]:
            output.append(f"- **{item['name']}** - ${item['value']:,} value")
            output.append(f"  - Delivery: {item['attention']} / {item['effort']}\n")
        
        if self.data["bonuses"]:
            output.append("\n### Bonuses\n")
            for bonus in self.data["bonuses"]:
                output.append(f"- 🎁 **{bonus['name']}** - ${bonus['value']:,} value")
                output.append(f"  - {bonus['description']}\n")
        
        output.append("\n---\n")
        output.append("## Enhancement Elements\n")
        
        output.append("### Guarantee\n")
        g = self.data["guarantee"]
        if g.get("name"):
            output.append(f"**{g['name']}**\n")
        output.append(f"Type: {g.get('type', 'TBD')}\n")
        if g.get("conditions"):
            output.append(f"Conditions: {g['conditions']}\n")
        if g.get("result"):
            output.append(f"Guaranteed result: {g['result']}\n")
        
        output.append("\n### Scarcity\n")
        output.append(f"{self.data['scarcity'] or 'Not configured'}\n")
        
        output.append("\n### Urgency\n")
        output.append(f"{self.data['urgency'] or 'Not configured'}\n")
        
        output.append("\n---\n")
        output.append("## Problems Solved\n")
        output.append(f"Total problems addressed: {len(self.data['problems'])}\n")
        
        # Group by category
        by_cat = {}
        for p in self.data["problems"]:
            cat = p["category"]
            if cat not in by_cat:
                by_cat[cat] = []
            by_cat[cat].append(p["problem"])
        
        for cat, problems in by_cat.items():
            output.append(f"\n### {cat} ({len(problems)})\n")
            for p in problems[:5]:  # Show first 5
                output.append(f"- {p}")
            if len(problems) > 5:
                output.append(f"- *...and {len(problems)-5} more*")
            output.append("")
        
        output.append("\n---\n")
        output.append("## Sales Presentation Summary\n")
        output.append(f"```")
        output.append(f"{self.data['name']}")
        output.append(f"")
        output.append(f"For: {self.data['avatar']}")
        output.append(f"Result: {self.data['dream_outcome']}")
        output.append(f"")
        output.append(f"WHAT'S INCLUDED:")
        for item in self.data["stack"]:
            output.append(f"✓ {item['name']} (${item['value']:,} value)")
        output.append(f"")
        if self.data["bonuses"]:
            output.append(f"BONUSES:")
            for bonus in self.data["bonuses"]:
                output.append(f"🎁 {bonus['name']} (${bonus['value']:,} value)")
            output.append(f"")
        output.append(f"─────────────────────────────")
        output.append(f"TOTAL VALUE: ${self.data['total_value']:,}")
        output.append(f"YOUR INVESTMENT: {self.data['price']}")
        output.append(f"─────────────────────────────")
        output.append(f"```\n")
        
        return "\n".join(output)
    
    def run(self):
        """Run the complete worksheet."""
        print("\n" + "=" * 60)
        print("   GRAND SLAM OFFER WORKSHEET")
        print("   Based on Alex Hormozi's $100M Offers")
        print("=" * 60)
        
        input("\nPress Enter to begin...")
        
        # Run all steps
        self.run_step_1_dream_outcome()
        self.run_step_2_problems()
        self.run_step_3_solutions()
        self.run_step_4_delivery()
        self.run_step_5_trim_and_stack()
        self.run_bonuses()
        self.run_guarantee()
        self.run_scarcity_urgency()
        self.run_naming()
        self.run_pricing()
        
        self.clear_screen()
        print("COMPLETE!")
        print("=" * 60)
        
        return self.generate_output()


def main():
    parser = argparse.ArgumentParser(
        description="Interactive Grand Slam Offer Worksheet Generator"
    )
    parser.add_argument(
        "--output", "-o",
        default="grand_slam_offer.md",
        help="Output filename (default: grand_slam_offer.md)"
    )
    args = parser.parse_args()
    
    worksheet = OfferWorksheet()
    output = worksheet.run()
    
    # Save to file
    with open(args.output, 'w') as f:
        f.write(output)
    
    print(f"\n✓ Offer saved to: {args.output}")
    print("\nPreview:")
    print("-" * 40)
    print(output[:1000] + "..." if len(output) > 1000 else output)


if __name__ == "__main__":
    main()
