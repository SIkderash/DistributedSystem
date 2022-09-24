import { Component, Input, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { CookieService } from 'ngx-cookie-service';
import { UserService } from '../user.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

    constructor(private userService: UserService, private route: Router, private cookieService : CookieService) {
    }
    username : string = "";
    password :string = "";
    
    ngOnInit(): void {
    }
   
    login(){
      if(this.username != "" && this.password != "")
      {
        console.log("logging in")
        var data = {
          username: this.username,
          password: this.password
        }

        this.userService.login(data).subscribe((response : any)=>{
          //alert("Logged In as " + this.username)
          console.log(response)
          this.cookieService.set('jwt', response['jwt'])
          this.authenticate();
        });

        this.route.navigate([''])
      }
      else
      {
        alert('Username or Password can not be blank!')
      }
    }
    authenticate(){
      this.userService.authenticate().subscribe((response: any) => {
          console.log(response)
          this.username = response['username']
          //console.log("ASDASD " + this.username)
          localStorage.setItem('username', String(this.username));
        },
      );
    }

    register(){
      this.route.navigate(['register'])
    }

}
