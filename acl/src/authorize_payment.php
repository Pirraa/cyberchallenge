<?php

session_start();

// The amount of money you currently have on your account
$account = $_SESSION['you']['amount'];
// The amount of money you want to pay
$amount = (int)$_GET['amount'];
if ($amount < 0) { exit("No stealing plz"); }

// Authorize payment, but only if you have enough money for it
if ($account - $amount >= 0) {
	array_unshift($_SESSION['payments'], $amount);
	header("Refresh: 1;url=finalize_payment.php");
	echo "Processing payment...";
} else {
	header("Refresh: 1; url=index.php");
	echo "Payment failed. Not enough money.";
}
