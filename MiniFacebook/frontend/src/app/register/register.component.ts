import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { UserService } from '../user.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {

  username : string = "";
  password :string = "";
  email : string = "";

  constructor(private userService : UserService, private route : Router) { }

  ngOnInit(): void {
  }
  
  register(){
    console.log("adding User")
    var data = {
      email:this.email,
      username:this.username,
      password:this.password
    }
    this.userService.register(data).subscribe(response=>{
      //this.toastr.success('Notification', response.toString());
      alert(response)
      this.route.navigate(['login'])
    });
  }

  login(){
    this.route.navigate(['login'])
  }
}
