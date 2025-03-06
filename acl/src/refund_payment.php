<?php

session_start();

header("Refresh:2; url=index.php");

$id = (int)$_GET['id'];

// Get payment data
if (!array_key_exists($id, $_SESSION['payments'])) {
    exit('This payment is not available for refund');
}

$amount = (int)$_SESSION['payments'][$id];
// Remove payment from authorized payments list
unset($_SESSION['payments'][$id]);
// (ignore this) rearrange array
$_SESSION['payments'] = array_values($_SESSION['payments']);

// Actual money transfer
$_SESSION['you']['amount'] += $amount;
$_SESSION['corp']['amount'] -= $amount;

echo "Payment succesfully refunded. You received $amount$.";
