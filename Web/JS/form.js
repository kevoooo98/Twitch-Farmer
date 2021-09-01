document.addEventListener("DOMContentLoaded", function(){
  document.getElementById('fav').addEventListener('change', changefav);
});

function changefav(){
  if (this.checked)
    this.value = 1;
  else
    this.value = 0;
}
