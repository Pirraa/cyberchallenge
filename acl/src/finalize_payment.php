<?php

session_start();

header("Refresh:2; url=index.php");

$id = (int)$_GET['id'];

// Get payment data
if (!array_key_exists(0, $_SESSION['payments'])) {
    exit('Payment failed. No payments to finalize.');
}

$amount = (int)$_SESSION['payments'][0];

if ($_SESSION['you']['amount'] - $amount >= 0) {
	// Actual money transfer
	$_SESSION['you']['amount'] -= $amount;
	$_SESSION['corp']['amount'] += $amount;

	echo "Payment successful. You paid $amount$.";
} else {
	echo "Payment failed. You do not have $amount on your account.";
}
