import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import {catchError, retry, map, filter, toArray} from 'rxjs/operators';

const baseURL = 'http://127.0.0.1:8000/api/higher_study/';

@Injectable({
  providedIn: 'root'
})

export class HigherstudyService {

  constructor(private httpClient: HttpClient) {
  }

  httpOptions = {
    headers: new HttpHeaders({'Content-Type': 'application/json'})
  };

  readAll(): Observable<any> {
    return this.httpClient.get(baseURL);
  }
}
