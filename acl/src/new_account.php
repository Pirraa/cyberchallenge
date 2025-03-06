<?php

session_start();

header("Refresh:2; url=index.php");

echo "Setting up an account and resetting your payments.<br/>";

$_SESSION['you']['amount'] = 100;
echo "You now have {$_SESSION['you']['amount']}$.<br/>";
$_SESSION['corp']['amount'] = 200;
echo "You currently payed {$_SESSION['corp']['amount']}$.<br/>";

$_SESSION['payments'] = array();

echo "Redirecting to your home page...";
