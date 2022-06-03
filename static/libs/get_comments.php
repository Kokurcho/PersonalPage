<?php
  header("Content-Type: text/html; charset=UTF-8");
  $count = $_POST['count'];
  $mysqli = new Mysqli('localhost', 'root', '', 'comments');
  $mysqli->query("SET NAMES utf8");
  $r = array();
  $result = $mysqli->query("SELECT * FROM comm WHERE id > $count");
  while($row = $result->fetch_assoc()) {
   $r[] = $row;
  }
  if(empty($r)) {
   echo "empty";
  } else {
   echo json_encode($r);
  }
?>