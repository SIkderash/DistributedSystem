
import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http"
import { Observable } from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class UserService {
  username!: any;

  constructor(private http: HttpClient) { }
  
  // API_URL_1 = 'http://127.0.0.1/auth'
  // API_URL_2 = 'http://127.0.0.1/status'
  // API_URL_3 = 'http://127.0.0.1/story'


  API_URL_1 = 'http://10.100.103.50/auth'
  API_URL_2 = 'http://10.100.103.50/status'
  API_URL_3 = 'http://10.100.103.50/story'

  register(val: any) {
    return this.http.post(this.API_URL_1 + '/register/', val);
  }
  login(val:any){
    return this.http.post(this.API_URL_1 +  '/login/', val, {
        withCredentials: true
    });
  }
  authenticate(){
      return this.http.get(this.API_URL_1 + '/user/', {withCredentials: true});
  }

  logout(){
    localStorage.removeItem('username')
    return this.http.post(this.API_URL_1 + '/logout/', {}, {withCredentials: true})
  }

  addStory(image:any) {
    return this.http.post(this.API_URL_3 + '/addStory/', image, {withCredentials: true});
  }

  getStories(): Observable<any[]> {
    return this.http.get<any[]>(this.API_URL_3 + '/stories/', {withCredentials: true});
  }

  postStatus(data : any){
    return this.http.post(this.API_URL_2 + '/addStatus/', data, {withCredentials: true});
  }

  getFeed(): Observable<any[]> {
    var data = {
      username : localStorage.getItem('username'),
    }
    return this.http.post<any[]>(this.API_URL_2 +  '/feed/', data, {withCredentials: true});
  }

  getEncodedImages(data : any): Observable<any> {
    return this.http.post<any[]>(this.API_URL_3 + '/story/', data, {withCredentials: true});
  }

}
