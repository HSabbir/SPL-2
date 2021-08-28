import {Component, Input, OnInit} from '@angular/core';

@Component({
  selector: 'app-single-people',
  templateUrl: './single-people.component.html',
  styleUrls: ['./single-people.component.scss']
})
export class SinglePeopleComponent implements OnInit {
  @Input() people!: any;
  constructor() {
  }

  ngOnInit(): void {
  }

}
