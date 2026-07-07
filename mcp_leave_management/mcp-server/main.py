from datetime import datetime
from typing import Dict, List, Any
from fastmcp import FastMCP

# Create the MCP Server
mcp = FastMCP("Leave Management System")

# In-memory database with diverse usage states
LEAVE_BALANCES: Dict[str, Dict[str, int]] = {
    "EMP001": {"Annual": 9, "Casual": 7, "Sick": 8},     # Total remaining: 24
    "EMP002": {"Annual": 20, "Casual": 10, "Sick": 10},  # Total remaining: 40 (MAXIMUM)
    "EMP003": {"Annual": 0, "Casual": 0, "Sick": 0},     # Total remaining: 0  (MINIMUM)
    "EMP004": {"Annual": 15, "Casual": 2, "Sick": 5},    # Total remaining: 22
}

LEAVE_REQUESTS: List[Dict[str, Any]] = [
    {
        "request_id": 1,
        "employee_id": "EMP001",
        "leave_type": "Annual",
        "start_date": "2026-05-01",
        "end_date": "2026-05-05",
        "status": "Approved"
    },
    {
        "request_id": 2,
        "employee_id": "EMP003",
        "leave_type": "Annual",
        "start_date": "2026-01-01",
        "end_date": "2026-01-15",
        "status": "Approved"
    },
    {
        "request_id": 3,
        "employee_id": "EMP003",
        "leave_type": "Casual",
        "start_date": "2026-03-10",
        "end_date": "2026-03-17",
        "status": "Approved"
    },
    {
        "request_id": 4,
        "employee_id": "EMP003",
        "leave_type": "Sick",
        "start_date": "2026-06-01",
        "end_date": "2026-06-10",
        "status": "Approved"
    },
    {
        "request_id": 5,
        "employee_id": "EMP004",
        "leave_type": "Casual",
        "start_date": "2026-04-12",
        "end_date": "2026-04-15",
        "status": "Approved"
    }
]

# --- 🛠️ NEW ANALYTICS TOOLS ---

@mcp.tool()
def get_total_employee_count() -> str:
    """
    Get the total number of employees registered in the leave system.
    """
    count = len(LEAVE_BALANCES)
    return f"Total registered employees in the system: {count}"


@mcp.tool()
def get_employee_with_max_leaves() -> str:
    """
    Find and retrieve the employee who has the highest total number of remaining leaves left.
    """
    if not LEAVE_BALANCES:
        return "No employees found in the system."
        
    # Find employee with highest sum of all leave types
    max_employee = max(LEAVE_BALANCES.keys(), key=lambda emp: sum(LEAVE_BALANCES[emp].values()))
    max_balances = LEAVE_BALANCES[max_employee]
    total_days = sum(max_balances.values())
    
    output = f"Employee with MAXIMUM remaining leaves: {max_employee}\n"
    output += f"Total remaining balance: {total_days} days\n"
    output += "\n".join(f"- {k}: {v} days" for k, v in max_balances.items())
    return output


@mcp.tool()
def get_employee_with_min_leaves() -> str:
    """
    Find and retrieve the employee who has the lowest total number of remaining leaves left (exhausted balances).
    """
    if not LEAVE_BALANCES:
        return "No employees found in the system."
        
    # Find employee with lowest sum of all leave types
    min_employee = min(LEAVE_BALANCES.keys(), key=lambda emp: sum(LEAVE_BALANCES[emp].values()))
    min_balances = LEAVE_BALANCES[min_employee]
    total_days = sum(min_balances.values())
    
    output = f"Employee with MINIMUM remaining leaves: {min_employee}\n"
    output += f"Total remaining balance: {total_days} days\n"
    output += "\n".join(f"- {k}: {v} days" for k, v in min_balances.items())
    return output

# --- 🛠️ EXISTING TOOLS ---

@mcp.tool()
def check_balances(employee_id: str) -> str:
    """Check remaining leave balances for a specific employee."""
    employee_id = employee_id.upper()
    if employee_id not in LEAVE_BALANCES:
        return f"Error: Employee ID {employee_id} not found."
    balances = LEAVE_BALANCES[employee_id]
    return f"Leave balances for {employee_id}:\n" + "\n".join(f"- {k}: {v} days remaining" for k, v in balances.items())


@mcp.tool()
def submit_leave_request(employee_id: str, leave_type: str, start_date: str, end_date: str) -> str:
    """Submit a new leave request for an employee."""
    employee_id = employee_id.upper()
    leave_type = leave_type.capitalize()
    
    if employee_id not in LEAVE_BALANCES:
        return f"Error: Employee ID {employee_id} not found."
    if leave_type not in LEAVE_BALANCES[employee_id]:
        return f"Error: Invalid leave type."
    
    try:
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        requested_days = (end - start).days + 1
        if requested_days <= 0:
            return "Error: End date must be after or equal to the start date."
    except ValueError:
        return "Error: Date must be in YYYY-MM-DD format."
        
    current_balance = LEAVE_BALANCES[employee_id][leave_type]
    if requested_days > current_balance:
        return f"Error: Insufficient balance."
        
    LEAVE_BALANCES[employee_id][leave_type] -= requested_days
    new_id = len(LEAVE_REQUESTS) + 1
    LEAVE_REQUESTS.append({
        "request_id": new_id, "employee_id": employee_id, "leave_type": leave_type,
        "start_date": start_date, "end_date": end_date, "status": "Pending"
    })
    return f"Success! Leave request ID #{new_id} created."

# --- 📂 MCP RESOURCES ---

@mcp.resource("leaves://requests/all")
def get_all_requests() -> str:
    """Get a complete historical list of all leave requests."""
    if not LEAVE_REQUESTS: return "No leave requests found."
    output = "📋 Global Leave Register:\n"
    for r in LEAVE_REQUESTS:
        output += f"- #{r['request_id']} | {r['employee_id']} | {r['leave_type']} | {r['start_date']} to {r['end_date']} | [{r['status']}]\n"
    return output

if __name__ == "__main__":
    mcp.run()