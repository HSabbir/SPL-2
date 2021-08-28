import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';

const baseURL = 'http://127.0.0.1:8000/api/profile/';

@Injectable({
  providedIn: 'root'
})

export class PeopleService {

  constructor(private httpClient: HttpClient) { }
  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };
  readAll(): Observable<any> {
    return this.httpClient.get(baseURL);
  }

  // read(id): Observable<any> {
  //   return this.httpClient.get(`${baseURL}/${id}`);
  // }
  //
  // create(data): void {
  //   data.price = parseFloat(data.price);
  //   data.quantityAvaiable = parseInt(data.quantityAvaiable, 10);
  //   this.httpClient.post(baseURL, data, this.httpOptions).subscribe(result => {
  //     this.allProducts = result;
  //   });
  // }
  //
  // update(data): void{
  //   this.httpClient.put(baseURL, data, this.httpOptions).subscribe(result => {});
  // }
  //
  // delete(id): Observable<any> {
  //   return this.httpClient.delete(`${baseURL}/${id}`);
  // }
}
