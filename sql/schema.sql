CREATE DATABASE IF NOT EXISTS checksite_logs;
USE checksite_logs;

CREATE TABLE IF NOT EXISTS http_status (
    id INT AUTO_INCREMENT PRIMARY KEY,
    hostname VARCHAR(50),
    log_date DATETIME,
    status_code INT,
    count INT,
    UNIQUE KEY unique_entry (hostname, log_date, status_code)
);

CREATE TABLE IF NOT EXISTS page_errors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    hostname VARCHAR(50),
    log_date DATETIME,
    url TEXT,
    error_type VARCHAR(100),
    raw_error TEXT,
    UNIQUE KEY unique_entry (hostname, log_date, url(255), error_type)
);
