<?php
  $name = $_POST['name'];
  $comment = $_POST['comment'];
  $mysqli = new Mysqli('localhost', 'root', '', 'comments');
  $mysqli->query("SET NAMES utf8");
  $mysqli->query("INSERT INTO `comm`(`name`, `comment`) VALUES('$name', '$comment')");
  
?>