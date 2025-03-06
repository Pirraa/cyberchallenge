<?php
if(isset($_GET['source'])){
    highlight_file(__FILE__);
    return;
}

header("Content-Security-Policy: default-src 'none'; style-src cdnjs.cloudflare.com");
if(isset($_GET['url']) && !is_array($_GET['url'])){
    $url = $_GET['url'];
    if (filter_var($url, FILTER_VALIDATE_URL) === FALSE) {
        die('Not a valid URL');
    }
    $parsed = parse_url($url);
    if (!in_array($parsed['scheme'], ['http','https'])){
        die('Not a valid URL');
    }
    echo file_get_contents($url);
    return;
}

?>