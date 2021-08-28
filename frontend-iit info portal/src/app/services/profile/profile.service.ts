import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';

const profileURL = 'http://127.0.0.1:8000/api/profile/';
const projectURL = 'http://127.0.0.1:8000/api/project/';
const researchURL = 'http://127.0.0.1:8000/api/research/';
const higerURL = 'http://127.0.0.1:8000/api/higher_study/';
const professionURL = 'http://127.0.0.1:8000/api/profession/';

@Injectable({
  providedIn: 'root'
})

export class ProfileService {

  constructor(private httpClient: HttpClient) { }
  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };
  readAll(): Observable<any> {
    return this.httpClient.get(profileURL);
  }
  readCompleteProfile(id: number): Observable<any> {
    return this.httpClient.get(`http://127.0.0.1:8000/api/profile/${id}/`);
  }
  getPreview(link: string): Observable<any>{
    const api = 'https://linkpreview.net/?key=066cc335feb24d42926c672e5cf0378e&q=' + link ;
    return this.httpClient.get(api);
  }
  create(data): Observable<any>{
    return this.httpClient.post(profileURL, data);
  }
}

