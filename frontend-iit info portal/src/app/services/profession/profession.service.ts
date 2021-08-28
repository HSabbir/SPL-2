import { Injectable } from '@angular/core';
import {Observable} from 'rxjs';
import {HttpClient} from '@angular/common/http';

const baseURL = 'http://127.0.0.1:8000/api/profession/';

@Injectable({
  providedIn: 'root'
})
export class ProfessionService {

  constructor(private httpClient: HttpClient) { }
  readAll(): Observable<any> {
    return this.httpClient.get(baseURL);
  }
  create(data): Observable<any> {
    return this.httpClient.post(baseURL, data);
  }
}
