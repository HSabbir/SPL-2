import { Component, OnInit } from '@angular/core';
import {PeopleService} from '../../services/people/people.service';

@Component({
  selector: 'app-people',
  templateUrl: './people.component.html',
  styleUrls: ['./people.component.scss']
})
export class PeopleComponent implements OnInit {
  peoples: any;
  constructor(private peopleService: PeopleService) {
    peopleService.readAll().subscribe(data => {
      this.peoples = data;
    });
  }

  ngOnInit(): void {
  }

}
