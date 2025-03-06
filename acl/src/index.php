<?php

session_start();

include 'includes/header.php';

if (isset($_SESSION['you']) && isset($_SESSION['corp'])) {
	echo "<div class='col-md-6'>
		<p>You currently have {$_SESSION['you']['amount']}$ in your account.</p>";
	echo "<p>You currently paid {$_SESSION['corp']['amount']}$.</p>";

	if ($_SESSION['corp']['amount'] <= 0) {
		echo "<code>".getenv('FLAG')."</code>";
	}
	echo "</div>";

	echo "<div class='col-md-6'><p>Create a new payment</p>
		<form action='authorize_payment.php' method='GET'>
			<label for='amount' value='Amount'>
			<input type='text' name='amount'/>
			<input type='submit' class='btn btn-primary'/>
		</form>";
	echo "<h1>Your payments</h1>
		<table>";

	echo "<tr>";	
	echo "<td>► 200$</td>";
	echo "<td>(Refund unavailable)</td>";
	echo "</tr>";	

	foreach ($_SESSION['payments'] as $id => $amount) {
		echo "<tr>";	
		echo "<td>► $amount$</td>";
		echo "<td><a href='refund_payment.php?id=$id'>Get refund</a></td>";
		echo "</tr>";	
	}
	echo "</table></div>";

} else {
	echo "<div class='col-md-6'><p>You currently don't have an account</p>";
}

echo "<p>Go <a href='new_account.php'>here</a> if you want a new account.<p></div>";

include 'includes/footer.php';

?>
