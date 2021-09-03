<?php

/**
 * Controlls DB Access
 */
class DBController
{

  private $dbuser = 'dbuser';
  private $dbpass = 'geheim1';
  private $dsn = 'mysql:dbname=twitchfarm;host=database';
  public $PDO ='';

  function __construct()
  {
    $this->PDO = new PDO($this->dsn, $this->dbuser, $this->dbpass);
  }

  function run_SQL($str_query){
    $PDO = $this->PDO;
    $statement = $PDO->prepare($str_query);
    $statement->execute();
  }

  function fetchquery($str_query){
    $PDO = $this->PDO;
    $statement = $PDO->prepare($str_query);
    $statement->execute();
    return $statement->fetchAll();
  }

}
