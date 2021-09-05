document.addEventListener("DOMContentLoaded", function(){
  document.getElementById('fav').addEventListener('change', changefav);
  document.querySelectorAll('[name="dlt-dataset"]').forEach(i=>{
    i.value = i.parentElement.parentElement.parentElement.firstChild.innerHTML;
  });
});

function changefav(){
  if (this.checked)
    this.value = 1;
  else
    this.value = 0;
}
