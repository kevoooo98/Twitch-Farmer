<?php

/**
 * Controlls DB Access
 */
class Tablecontroller extends DBController
{

  private $query = "SELECT * FROM streams s ;";

  function __construct($dbc)
  {
    $this->dbc = $dbc;
  }

  function build_table(){
    $db_data = $this->dbc->fetchquery($this->query);
    if (!empty($db_data)){
      $th = array_map(function($key){
        return '<th>'.$key.'</th>';
      },array_keys($db_data[0]));
      $tr = array_map(function($data){
        $td = array_map(function($cell){
          return '<td>'.$cell.'</td>';
        },($data));
        return '<tr>'.implode('',$td).'<td><form method="POST"><input type="hidden" name="dlt-dataset"></input><button type="submit">&#128465;</button></form></td></tr>';
      },($db_data));


      return ('<thead><tr>'.implode('',$th).'</tr></thead><tbody>'.implode('',$tr).'</tbody>');
    } else
      return '';
  }
}
