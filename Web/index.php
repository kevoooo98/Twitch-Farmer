<?php
  ini_set('display_errors', 1);
  error_reporting(-1);

  define("BASE_DIR", __DIR__);

  include_once(BASE_DIR.'/controller/DBController.php');
  $DBController = new DBController();

  if(!empty($_POST)){
    if(isset($_POST['pushdata'])){
      include_once(BASE_DIR.'/controller/pushController.php');
      $pushController = new PushController($_POST);
      $pushquery = $pushController->get_push_query();
      $DBController->run_SQL($pushquery);
      unset($_POST);
    }
  }

  $html = file_get_contents(BASE_DIR . '/html/form.html');

  include_once(BASE_DIR.'/controller/Tablecontroller.php');
  $tc = new Tablecontroller($DBController);
  
  $html = strtr($html,['{{table}}' => $tc->get_tabledata()]);

  echo $html;
