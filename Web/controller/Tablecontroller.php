<?php

/**
 * Controlls DB Access
 */
class Tablecontroller extends DBController
{

  private $query = "SELECT * FROM streams;";

  function __construct($dbc)
  {
    $this->dbc = $dbc;
  }

  function get_tabledata(){
    return $this->dbc->fetchquery($this->query);
  }

  function build_table(){
    $db_data = $this->get_tabledata();

      $th = array_map(function($key){
        return '<th>'.$key.'</th>';
      },array_keys($db_data));
      $tr = array_map(function($data){
        $td = array_map(function($cell){
          return '<td>'.$cell.'</td>';
        },($data));
        return '<tr>'.implode('',$td).'</tr>';
      },($db_data));

    return ('<tr>'.explode('',$th).'</tr>'.explode('',$tr));
  }
}
