import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { UserService } from '../user.service';

@Component({
  selector: 'app-story',
  templateUrl: './story.component.html',
  styleUrls: ['./story.component.css']
})
export class StoryComponent implements OnInit {

  image:any
  uid:any

  constructor(private userService : UserService, private route : Router) { }

  ngOnInit(): void {
  }

  onChanged(event:any){
    this.image = event.target.files[0];
  }
  
  uploadata = new FormData();
  addStory(){
      this.userService.addStory("ash1971").subscribe(response=>{
        this.uid = response.toString()
        this.uploadata.append('image', this.image);
        this.uploadata.append('file_name', this.uid);
        this.uploadPhoto();
      });
  }

  uploadPhoto(){
    this.userService.addStory(this.uploadata).subscribe(response=>{
      alert(response.toString())
      this.route.navigate(['story'])
    });
  }
}
