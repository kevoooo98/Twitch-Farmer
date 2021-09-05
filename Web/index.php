<?php
  define("BASE_DIR", __DIR__);

  include_once(BASE_DIR.'/controller/DBController.php');
  $DBController = new DBController();

  if(!empty($_POST)){
    include_once(BASE_DIR.'/controller/queryController.php');
    $queryController = new QueryController();

    if(isset($_POST['dlt-dataset'])){
      $pushquery = $queryController->get_delete_query($_POST);
      $DBController->run_SQL($pushquery);
    }
    if(isset($_POST['pushdata'])){
      $pushquery = $queryController->get_push_query($_POST);
      $DBController->run_SQL($pushquery);
    }
    unset($_POST);
  }


  include_once(BASE_DIR.'/controller/Tablecontroller.php');
  $tc = new Tablecontroller($DBController);

  $html = file_get_contents(BASE_DIR . '/html/form.html');
  $html = strtr($html,['{{table}}' => $tc->build_table()]);

  echo $html;
