<?php

/**
 *
 */
class QueryController
{

  private $pushquery_path = BASE_DIR . "/SQL/pushdata.sql";
  private $dltquery_path = BASE_DIR . "/SQL/dltdata.sql";

  function __construct()
  {

  }

  function get_push_query($postdata){
    $data['{{url}}']        = $postdata['url'];
    $data['{{watchtime}}']  = $postdata['watchtime'];
    $data['{{fav}}']        = isset($postdata['fav']) ? 1 : 0;
    $sql_tpl = file_get_contents($this->pushquery_path);
    $sql = strtr($sql_tpl, $data);
    return $sql;
  }

  function get_delete_query($postdata){
    $data['{{id}}']        = $postdata['dlt-dataset'];
    $sql_tpl = file_get_contents($this->dltquery_path);
    $sql = strtr($sql_tpl, $data);
    return $sql;
  }
}
