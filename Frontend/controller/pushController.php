<?php

/**
 *
 */
class PushController
{

  private $pushquery_path = BASE_DIR . "/SQL/pushdata.sql";

  function __construct($postdata)
  {
    $this->data['{{url}}']        = $postdata['url'];
    $this->data['{{watchtime}}']  = $postdata['watchtime'];
    $this->data['{{fav}}']        = isset($postdata['fav']) ? 1 : 0;
  }

  function get_push_query(){
  	 $sql_tpl = file_get_contents($this->pushquery_path);
  	 $sql = strtr($sql_tpl, $this->data);
	   return $sql;
  }
}
