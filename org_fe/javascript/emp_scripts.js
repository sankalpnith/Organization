//var url = 'http://127.0.0.1:8000/'
var url = 'http://18.224.171.135:8000/'
var emp_read = 'employee_read'
var emp_create = 'employee_create'
var emp_edit = 'employee_edit'
var emp_delete = 'employee_delete'
var room_read = 'conf_room_read'
var room_create = 'conf_room_create'
var room_edit = 'conf_room_edit'
var room_delete = 'conf_room_delete'

function UserLogin() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
         if (this.readyState === 4 && this.status == 201) {
             var obj = JSON.parse(this.responseText)
             window.sessionStorage.setItem("token", obj.token)
             window.sessionStorage.setItem("userId", obj.userId)
             window.sessionStorage.setItem("userName", obj.user_name)
             window.sessionStorage.setItem("role", obj.role)
             window.sessionStorage.setItem("permissions", obj.permissions)
             window.location.href = "employee.html"
         }else if (this.readyState === 4){
         	alert(this.responseText)
         }
    };
    xhttp.open("POST", url + "login/", true);
    xhttp.setRequestHeader("Content-type", "application/json");
    xhttp.send(JSON.stringify({"email":document.getElementById("login").value, "password":document.getElementById("password").value}));
}


function UserLogout() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
         if (this.readyState === 4 && this.status == 204) {
             window.sessionStorage.clear()
             window.location.href = "index.html"
         }
    };
    xhttp.open("DELETE", url + "logout/", true);
    xhttp.setRequestHeader("Content-type", "application/json");
    xhttp.setRequestHeader("Authorization", "Bearer " + window.sessionStorage.getItem("token"));
    xhttp.send();
}

// Init function 
function onStart(){
	var xhttp = new XMLHttpRequest();
	var mydata = []
    xhttp.onreadystatechange = function() {
         if (this.readyState === 4 && this.status == 200) {
             window.sessionStorage.setItem("roles", this.responseText) 
          }
    };
    xhttp.open("GET", url + "roles/", true);
    xhttp.setRequestHeader("Content-type", "application/json");
    xhttp.setRequestHeader("Authorization", "Bearer " + window.sessionStorage.getItem("token"));
    xhttp.send();

    roomButton = document.getElementById("roomButton");
    if (window.sessionStorage.getItem("permissions").includes(room_read)){
    	roomButton.style.display="block"
    }
    empButton = document.getElementById("empButton");
    if (window.sessionStorage.getItem("permissions").includes(emp_read)){
    	empButton.style.display="block"
    }
    addEmpButton = document.getElementById("addEmpButton");
    if (window.sessionStorage.getItem("permissions").includes(emp_create)){
    	addEmpButton.style.display="block"
    }
    addRoomButton = document.getElementById("addRoomButton");
    if (window.sessionStorage.getItem("permissions").includes(room_create)){
    	addRoomButton.style.display="block"
    }
    document.getElementById('userName').textContent = "Hello " + window.sessionStorage.getItem("userName")
    document.getElementById('roleName').textContent = window.sessionStorage.getItem("role")
}

function openAddEmployeeModal() {
	var modal = document.getElementById("createEmpModal");
	var span = document.getElementsByClassName("closeCreateEmp")[0];
  	modal.style.display = "block";

	document.getElementById("create_emp_id").value = "";
  	document.getElementById("create_name").value = "";
  	document.getElementById("create_email").value = "";
  	document.getElementById("create_mobile_number").value = "";
  	document.getElementById("create_team").value = "";
	document.getElementById("create_position").value = "";


  	var select = document.getElementById("create_role")
	select.innerHTML=""
	roles = JSON.parse(window.sessionStorage.getItem("roles"))	
	for(var i=0; i<roles.length; i++){
		opt = document.createElement("option");
		opt.value = roles[i].id;
		opt.textContent = roles[i].name;
		select.appendChild(opt);
	}

	var save = document.getElementById("CreateEmp");
	save.onclick = function(){
		obj = {}
		obj['emp_id'] = document.getElementById("create_emp_id").value
		obj['name'] = document.getElementById("create_name").value
		obj['email'] = document.getElementById("create_email").value
		obj['mobile_number'] = document.getElementById("create_mobile_number").value
		obj['team'] = document.getElementById("create_team").value
		obj['position'] = document.getElementById("create_position").value
		obj['role'] = document.getElementById("create_role").value
		var xhttp = new XMLHttpRequest();
	var mydata = []
    xhttp.onreadystatechange = function() {
         if (this.readyState === 4 && this.status == 201) {
             listEmployees();
             modal.style.display = "none";
             
         }else if(this.readyState === 4){
         	alert(this.responseText)
         }
    };
    xhttp.open("POST", url + "employees/", true);
    xhttp.setRequestHeader("Content-type", "application/json");
    xhttp.setRequestHeader("Authorization", "Bearer " + window.sessionStorage.getItem("token"));
    xhttp.send(JSON.stringify(obj));
	}

	span.onclick = function() {
  	modal.style.display = "none";
	}
	window.onclick = function(event) {
  		if (event.target == modal) {
    		modal.style.display = "none";
  		}
	}
}


function showEmpTable() {
  var x = document.getElementById('emp_table_div');
  var y = document.getElementById('room_table_div');
  if (x.style.display === "none") {
  	y.style.display = "none";
    x.style.display = "block";
    listEmployees();
  } 
}
function showRoomTable() {
  var x = document.getElementById("emp_table_div");
  x.style.display = "none";
  var y = document.getElementById("room_table_div");
  if (y.style.display === "none") {
  	x.style.display = "none";
    y.style.display = "block";
    listRooms();
  } 
  
}

function listEmployees() {
	var xhttp = new XMLHttpRequest();
	var mydata = []
    xhttp.onreadystatechange = function() {
         if (this.readyState === 4 && this.status == 200) {
             mydata = JSON.parse(this.responseText)
             const table = document.getElementById("emp_body");
             table.innerHTML=""
    		 mydata.forEach( item => {
      		 let row = table.insertRow();
      		 let empId = row.insertCell(0);
      		 empId.innerHTML = item.emp_id;
             let name = row.insertCell(1);
             name.innerHTML = item.name;
             let email = row.insertCell(2);
             email.innerHTML = item.email;
             let number = row.insertCell(3);
             number.innerHTML = item.mobile_number;
             let position = row.insertCell(4);
             position.innerHTML = item.position;
             let team = row.insertCell(5);
             team.innerHTML = item.team;
			 
			 if (window.sessionStorage.getItem("permissions").includes(emp_delete)){
    			let del_button = row.insertCell(6)
    			del_button.innerHTML = "<button type='button' onclick='deleteEmpRow(" + '"' + item.id + '"' + ")' >Delete</button><br>";
    		}
		     if (window.sessionStorage.getItem("permissions").includes(emp_edit)){
    			let edit_button = row.insertCell(6)
		     	edit_button.innerHTML = "<button type='button' onclick='openEditEmployeeModal(" + JSON.stringify(item) + ")' >Edit</button><br>";
    		}
		     
    });
         }
    };
    xhttp.open("GET", url +  "employees/", true);
    xhttp.setRequestHeader("Content-type", "application/json");
    xhttp.setRequestHeader("Authorization", "Bearer " + window.sessionStorage.getItem("token"));
    xhttp.send();
}

function deleteEmpRow(id){
	var xhttp = new XMLHttpRequest();
	var mydata = []
    xhttp.onreadystatechange = function() {
         if (this.readyState === 4 && this.status == 204) {
             listEmployees()
         }else if (this.readyState === 4){
         	alert("Delete Failed")
         }
    };
    xhttp.open("DELETE", url + "employees/"+ id+ "/", true);
    xhttp.setRequestHeader("Content-type", "application/json");
    xhttp.setRequestHeader("Authorization", "Bearer " + window.sessionStorage.getItem("token"));
    xhttp.send();
}



function openEditEmployeeModal(item) {
	var modal = document.getElementById("editEmpModal");
	// Get the <span> element that closes the modal
	var span = document.getElementsByClassName("closeEditEmp")[0];
  	modal.style.display = "block";

  	document.getElementById("emp_id").value = item.emp_id;
  	document.getElementById("name").value = item.name;
  	document.getElementById("email").value = item.email;
  	document.getElementById("mobile_number").value = item.mobile_number;
  	document.getElementById("team").value = item.team;
	document.getElementById("position").value = item.position;

	var select = document.getElementById("role")
	select.innerHTML=""
	roles = JSON.parse(window.sessionStorage.getItem("roles"))
	for(var i=0; i<roles.length; i++){
		opt = document.createElement("option");
		opt.value = roles[i].id;
		opt.textContent = roles[i].name;
		select.appendChild(opt);
		if(opt.value === item.role_id){
			select.options[i].selected=true
		}
	}
	var save = document.getElementById("EditEmp");
	save.onclick = function(){
		obj = {}
		obj['name'] = document.getElementById("name").value
		obj['email'] = document.getElementById("email").value
		obj['mobile_number'] = document.getElementById("mobile_number").value
		obj['team'] = document.getElementById("team").value
		obj['position'] = document.getElementById("position").value
		obj['role'] = document.getElementById("role").value
		var xhttp = new XMLHttpRequest();
	var mydata = []
    xhttp.onreadystatechange = function() {
         if (this.readyState === 4 && this.status == 200) {
             listEmployees();
             modal.style.display = "none";
             
         }else if (this.readyState === 4){
         	alert(this.responseText)
         }
    };
    xhttp.open("PUT", url + "employees/" + item.id + "/", true);
    xhttp.setRequestHeader("Content-type", "application/json");
    xhttp.setRequestHeader("Authorization", "Bearer " + window.sessionStorage.getItem("token"));
    xhttp.send(JSON.stringify(obj));
	}
	span.onclick = function() {
  	modal.style.display = "none";
	}

	window.onclick = function(event) {
  		if (event.target == modal) {
    		modal.style.display = "none";
  		}
	}
}


function listRooms() {
	var xhttp = new XMLHttpRequest();
	var mydata = []
    xhttp.onreadystatechange = function() {
         if (this.readyState === 4 && this.status == 200) {
             mydata = JSON.parse(this.responseText)
             const table = document.getElementById("room_body");
             table.innerHTML=""
    		 mydata.forEach( item => {
      		 let row = table.insertRow();
      		 let roomId = row.insertCell(0);
      		 roomId.innerHTML = item.room_id;
             let name = row.insertCell(1);
             name.innerHTML = item.name;
             let email = row.insertCell(2);
             email.innerHTML = item.booking_email;
             let sitting = row.insertCell(3);
             sitting.innerHTML = item.sitting_count;
             let status = row.insertCell(4);
             status.innerHTML = item.status;
             if (window.sessionStorage.getItem("permissions").includes(room_delete)){
    			let del_button = row.insertCell(5)
		     	del_button.innerHTML = "<button type='button' onclick='deleteRoomRow(" + '"' + item.id + '"' + ")' >Delete</button><br>";
    		}
    		if (window.sessionStorage.getItem("permissions").includes(room_edit)){
    			let edit_button = row.insertCell(5)
		     	edit_button.innerHTML = "<button type='button' onclick='openEditRoomModal(" + JSON.stringify(item) + ")' >Edit</button><br>";
    		}
          });
         }
    };
    xhttp.open("GET", url + "rooms/", true);
    xhttp.setRequestHeader("Content-type", "application/json");
    xhttp.setRequestHeader("Authorization", "Bearer " + window.sessionStorage.getItem("token"));
    xhttp.send();
}

function deleteRoomRow(id){
	var xhttp = new XMLHttpRequest();
	var mydata = []
    xhttp.onreadystatechange = function() {
         if (this.readyState === 4 && this.status == 204) {
             listRooms()
         }else if (this.readyState === 4){
         	alert("Delete Failed")
         }
    };
    xhttp.open("DELETE", url + "rooms/"+ id+ "/", true);
    xhttp.setRequestHeader("Content-type", "application/json");
    xhttp.setRequestHeader("Authorization", "Bearer " + window.sessionStorage.getItem("token"));
    xhttp.send();
}

function openAddRoomModal() {
	var modal = document.getElementById("createRoomModal");
	var span = document.getElementsByClassName("closeCreateRoom")[0];
  	modal.style.display = "block";

  	document.getElementById("create_room_id").value = "";
  	document.getElementById("create_room_name").value = "";
  	document.getElementById("create_booking_email").value = "";
  	document.getElementById("create_capacity").value = "";

	var save = document.getElementById("createRoom");
	save.onclick = function(){
		obj = {}
		obj['room_id'] = document.getElementById("create_room_id").value
		obj['name'] = document.getElementById("create_room_name").value
		obj['booking_email'] = document.getElementById("create_booking_email").value
		obj['sitting_count'] = document.getElementById("create_capacity").value
		var xhttp = new XMLHttpRequest();
	var mydata = []
    xhttp.onreadystatechange = function() {
         if (this.readyState === 4 && this.status == 201) {
             listRooms();
             modal.style.display = "none";
             
         }else if (this.readyState === 4){
         	alert(this.responseText)
         }
    };
    xhttp.open("POST", url + "rooms/", true);
    xhttp.setRequestHeader("Content-type", "application/json");
    xhttp.setRequestHeader("Authorization", "Bearer " + window.sessionStorage.getItem("token"));
    xhttp.send(JSON.stringify(obj));
	}

	span.onclick = function() {
  	modal.style.display = "none";
	}
	window.onclick = function(event) {
  		if (event.target == modal) {
    		modal.style.display = "none";
  		}
	}
}

function openEditRoomModal(item) {
	var modal = document.getElementById("editRoomModal");
	// Get the <span> element that closes the modal
	var span = document.getElementsByClassName("closeEditRoom")[0];
  	modal.style.display = "block";

  	document.getElementById("edit_room_id").value = item.room_id;
  	document.getElementById("edit_room_name").value = item.name;
  	document.getElementById("edit_booking_email").value = item.booking_email;
  	document.getElementById("edit_capacity").value = item.sitting_count;

	var save = document.getElementById("editRoom");
	save.onclick = function(){
		obj = {}
		obj['name'] = document.getElementById("edit_room_name").value
		obj['booking_email'] = document.getElementById("edit_booking_email").value
		obj['sitting_count'] = document.getElementById("edit_capacity").value
		var xhttp = new XMLHttpRequest();
	var mydata = []
    xhttp.onreadystatechange = function() {
         if (this.readyState === 4 && this.status == 200) {
             listRooms();
             modal.style.display = "none";
             
         }else if (this.readyState === 4){
         	alert(this.responseText)
         }
    };
    xhttp.open("PUT", url + "rooms/" + item.id + "/", true);
    xhttp.setRequestHeader("Content-type", "application/json");
    xhttp.setRequestHeader("Authorization", "Bearer " + window.sessionStorage.getItem("token"));
    xhttp.send(JSON.stringify(obj));
	}
	span.onclick = function() {
  	modal.style.display = "none";
	}

	window.onclick = function(event) {
  		if (event.target == modal) {
    		modal.style.display = "none";
  		}
	}
}