-- ============================================================================
-- DATABASE SETUP: PostgreSQL Synthetic Logs for Data Retriever Agent
-- ============================================================================

-- Step 1: Create the logs table
CREATE TABLE ai_support_logs (
    log_id SERIAL PRIMARY KEY,
    timestamp TIMESTAMPTZ NOT NULL,
    org_id VARCHAR(50) NOT NULL,
    org_name VARCHAR(100),
    service_tag VARCHAR(50),
    level VARCHAR(20),
    device_ip VARCHAR(50),
    device_name VARCHAR(100),
    message TEXT
);

-- Step 2: Create an index to optimize search performance (similar to ElasticSearch behavior)
CREATE INDEX idx_logs_org_tag ON ai_support_logs(org_id, service_tag);

-- Step 3: Insert synthetic (mock) logs for testing the AI Agent
INSERT INTO ai_support_logs (timestamp, org_id, org_name, service_tag, level, device_ip, device_name, message) VALUES
-- Normal Printer Operation
('2026-04-08 17:40:00+03', 'org_998877', 'Global Burger - NY', 'SPOOLER', 'info', '10.0.0.15', 'iPad Front Desk', '[M][SPOOLER] jobId=88d669971679d4fa0500570d is start printing'),
('2026-04-08 17:40:05+03', 'org_998877', 'Global Burger - NY', 'SPOOLER', 'info', '10.0.0.15', 'iPad Front Desk', '[M][SPOOLER][10.0.0.200][Kitchen] Job <requestId = BA8B8519> completed successfully, result code = 0'),

-- INCIDENT 1: Network Failure in the Kitchen
('2026-04-08 17:42:10+03', 'org_998877', 'Global Burger - NY', 'Network', 'warn', '10.0.0.16', 'iPad Kitchen', '[M][NETWORK MONITOR][Connectivity] Status = Weak Signal'),
('2026-04-08 17:42:15+03', 'org_998877', 'Global Burger - NY', 'Network', 'error', '10.0.0.16', 'iPad Kitchen', '[M][INAC][Network][WiFi][Monitor] Network status changed: Offline'),
('2026-04-08 17:42:16+03', 'org_998877', 'Global Burger - NY', 'Network', 'info', '10.0.0.16', 'iPad Kitchen', '[B][INAC][NETWORK MONITOR][Connectivity] Status = No WiFi'),

-- CASCADING FAILURE: Spooler cannot reach the kitchen printer due to network drop
('2026-04-08 17:43:00+03', 'org_998877', 'Global Burger - NY', 'SPOOLER', 'info', '10.0.0.15', 'iPad Front Desk', '[M][SPOOLER][10.0.0.200][Kitchen] Detected new printer job requestId = CC9C9519. Moved the job to status inProgress'),
('2026-04-08 17:43:10+03', 'org_998877', 'Global Burger - NY', 'SPOOLER', 'warn', '10.0.0.15', 'iPad Front Desk', '[M][SPOOLER][10.0.0.200][Kitchen] Job timeout after 10000ms. Retrying...'),
('2026-04-08 17:43:25+03', 'org_998877', 'Global Burger - NY', 'SPOOLER', 'error', '10.0.0.15', 'iPad Front Desk', '[M][SPOOLER][10.0.0.200][Kitchen] Job <requestId = CC9C9519> FAILED. Printer host unreachable. Result code = -1004'),
('2026-04-08 17:43:40+03', 'org_998877', 'Global Burger - NY', 'SPOOLER', 'error', '10.0.0.15', 'iPad Front Desk', '[M][SPOOLER][10.0.0.200][Kitchen] Job <requestId = DD0D0000> FAILED. Printer host unreachable. Result code = -1004'),

-- INCIDENT 2: Tablet/MDM Access Issues
('2026-04-08 17:45:00+03', 'org_998877', 'Global Burger - NY', 'MDM Autonomous Single App Mode', 'warn', '10.0.0.18', 'iPad Bar', '[B][MDM Autonomous Single App Mode] - guidedAccessDidChange Notification called with UIAccessibility.isGuidedAccessEnabled = false'),
('2026-04-08 17:45:05+03', 'org_998877', 'Global Burger - NY', 'MDM Autonomous Single App Mode', 'error', '10.0.0.18', 'iPad Bar', '[B][MDM Autonomous Single App Mode] - Failed to switch from Unknown
