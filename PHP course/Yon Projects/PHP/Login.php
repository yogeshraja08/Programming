<?php
if(!isset($_POST['submit'])){
$user = $_POST['username'];
$pass = $_POST['password'];

$con = mysqli_connect("localhost:3306","root","","Projects");
$sql = "select * from login where username = '$user' and password = '$pass'";
$result = mysqli_query($con,$sql);
$output = mysqli_num_rows($result);

if ($output>0){
    echo "login successful!";
}
else{
    echo "login failed!";
}
}

?>