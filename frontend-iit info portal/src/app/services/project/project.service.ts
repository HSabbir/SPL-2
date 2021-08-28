import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import {catchError, retry, map, filter, toArray} from 'rxjs/operators';

const baseURL = 'http://127.0.0.1:8000/api/project/';
const domainUrl = 'http://127.0.0.1:8000/api/domain/';
const environmentURL = 'http://127.0.0.1:8000/api/environment/';
const technology = 'http://127.0.0.1:8000/api/tools_and_technology/';


@Injectable({
  providedIn: 'root'
})

export class ProjectService {

  constructor(private httpClient: HttpClient) { }
  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/x-www-form-urlencoded' })
  };
  readAll(): Observable<any> {
    return this.httpClient.get(baseURL);
  }
  create(data): Observable<any> {
    return this.httpClient.post(baseURL, this.httpOptions, data);
  }
  readAllDOmain(): Observable<any> {
    return this.httpClient.get(domainUrl);
  }
  readAllEnvironment(): Observable<any> {
    return this.httpClient.get(environmentURL);
  }
  readAllTechnology(): Observable<any> {
    return this.httpClient.get(technology);
  }
  filterByUserId(id: number): any{
    return this.readAll().pipe (map(items =>
      items.filter(item => item.user[0].id === id ))).subscribe(data => {
        console.log(data);
    });
  }
  // projectByUserId(id: number): any {
  //   this.readAll().pipe(
  //     map(arr =>
  //       arr.filter( r => r.user.id === id )
  //     )
  //   ).subscribe( results => console.log('Filtered results:', results));
  //   return true;
  // }

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
