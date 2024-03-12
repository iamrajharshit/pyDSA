'''Implement a prototype service to automate the detection and replacement of faulty servers to Improve the availability of an application.

There are in servers with Ids s1, s2, sn, and an array of strings, logs of size m. Log format is "<server_ld> <success/error>", the id of the server, and the status of the processed request. If a particular server id logs an error for three consecutive requests, it is considered faulty and is replaced with a new server with the same id.

Given in and the array logs, find the number of times a faulty server was replaced.
Example

Suppose n = 2 and logs = ['s1 error", "s1 error", "s2 error", "s1 error", "s1 error", "s2 success"]'''


def replace_faulty_servers(n, logs):
  """
  Simulates a service to detect and replace faulty servers.

  Args:
      n: The number of servers.
      logs: A list of strings representing server logs.

  Returns:
      The number of times faulty servers were replaced.
  """

  # Initialize error counts and replacement count
  error_counts = [0] * n
  replacements = 0

  for log in logs:
    # Extract server ID and message type
    server_id, message_type = log.split()
    server_id = int(server_id[1:])  # Remove leading "s"

    # Update error count based on message type
    if message_type == "error":
      error_counts[server_id - 1] += 1

      # Check for 3 consecutive errors and replace server
      if error_counts[server_id - 1] == 3:
        error_counts[server_id - 1] = 0  # Reset error count for replaced server
        replacements += 1

    # Reset error count on encountering success message
    elif message_type == "success":
      error_counts[server_id - 1] = 0

  return replacements

# Example usage
logs = [
  "s1 error",
  "s1 error",
  "s2 error",
  "s1 error",
  "s1 error",
  "s2 success"
]

replacements = replace_faulty_servers(2, logs)
print(f"Number of server replacements: {replacements}")
