function info(){
	var myinfo = JSON.parse(info);
	alert(myinfo[0].pressure);
	alert(myinfo[0].last_update);
	alert(myinfo[0].temperature);
	alert(myinfo[0].humidity);
}