<?php

if(isset($_GET['s0urc3_c0d3'])) {
        echo preg_replace('/CCIT\{[a-zA-Z0-9-_]*\}/', 'redacted', highlight_file(__DIR__.'/index.php', true));
        die();
}

$s3cr3t_c0nt3nt = 'CCIT{redacted}';
if(false) {
        // You will never get here
        echo $s3cr3t_c0nt3nt;
}

// Supporting many different methods, we don't judge
parse_str(file_get_contents('php://input'), $data);
if($_SERVER['REQUEST_METHOD'] === 'POST') {
        $message = htmlspecialchars($data['message']);
        echo $message;
} else if($_SERVER['REQUEST_METHOD'] === 'GET' && isset($_GET['message'])) {
        $message = htmlspecialchars($_GET['message']);
        echo $message;
} else if($_SERVER['REQUEST_METHOD'] === 'PUT') {
        $message = htmlspecialchars($data['message']);
        echo $message;
} else if($_SERVER['REQUEST_METHOD'] === 'PATCH') {
        $message = htmlspecialchars($data['message']);
        echo $$message;
} else if($_SERVER['REQUEST_METHOD'] === 'DELETE') {
        $message = htmlspecialchars($data['message']);
        echo $message;
} else {
?>
<!-- for debug ?s0urc3_c0d3 -->

<h1>Welcome! Write a message!</h1>
<form action="/index.php" method="POST">
<input type="text" name="message">
<input type="submit" name="send" value="send">
</form>
<?php
}
