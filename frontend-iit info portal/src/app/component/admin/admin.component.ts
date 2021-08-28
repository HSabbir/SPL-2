import { Component, OnInit } from '@angular/core';
import {HttpClient} from '@angular/common/http';

@Component({
  selector: 'app-admin',
  templateUrl: './admin.component.html',
  styleUrls: ['./admin.component.scss']
})
export class AdminComponent implements OnInit {
  items = [
    {id: 1, name: 'Python'},
    {id: 2, name: 'Node Js'},
    {id: 3, name: 'Java'},
    {id: 4, name: 'PHP', disabled: true},
    {id: 5, name: 'Django'},
    {id: 6, name: 'Angular'},
    {id: 7, name: 'Vue'},
    {id: 8, name: 'ReactJs'},
  ];
  selected = [
  ];
  // title = 'ng-select-filter-demo';
  //
  // userList = [];
  // selectedUser: number;
  //
  constructor(
     private http: HttpClient
   ) { }
  //
  // // tslint:disable-next-line:typedef
   ngOnInit(): void {
   }
  //
  // // Fetching users data
  // getUsersList(): any {
  //   this.http
  //     .get<any>('https://jsonplaceholder.typicode.com/users')
  //     .subscribe(response => {
  //       this.userList = response.map(o => {
  //         o.search_label =
  //           `${o.id} ${o.name} ${o.username} ${o.email} ${o.phone} ${o.website} ${o.phone} ${o.address.street} ${o.address.suite} ${o.address.city} ${o.address.zipcode}`
  //         return o;
  //       });
  //       console.log(this.userList);
  //     }, error => {
  //       console.log(error);
  //     });
  // }
  // customSearchFn(term: string, item: any): any {
  //   term = term.toLowerCase();
  //
  //   const splitTerm = term.split(' ').filter(t => t);
  //
  //   const isWordThere = [];
  //
  //   // Pushing True/False if match is found
  //   // tslint:disable-next-line:variable-name
  //   splitTerm.forEach(arr_term => {
  //     const search = item.search_label.toLowerCase();
  //     // tslint:disable-next-line:triple-equals
  //     isWordThere.push(search.indexOf(arr_term) != -1);
  //   });
  //
  //   // tslint:disable-next-line:variable-name
  //   const all_words = (this_word) => this_word;
  //   // Every method will return true if all values are true in isWordThere.
  //   return isWordThere.every(all_words);
  // }
}
