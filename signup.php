<?php
  $name = $_POST['name']; 
  $email = $_POST['email']; 
  $password = $_POST['password']; 

  $conn = new mysqli('localhost', 'root','','leefy'); 
  if($conn->connect_error){
    die('connection error'.$conn_>connect_error);
  }else{
    $stmt = $conn->prepare("insert into users(name, email, password)values(?,?,?)"); 
    $stmt->bind_param("sss", $name, $email, $password); 
    $stmt->execute(); 
    echo "success"; 
    $stmt->close(); 
    $conn->close(); 
  }
?>
