import {Component, Input, OnInit} from '@angular/core';

@Component({
  selector: 'app-higher-study-card',
  templateUrl: './higher-study-card.component.html',
  styleUrls: ['./higher-study-card.component.scss']
})
export class HigherStudyCardComponent implements OnInit {
  @Input()higherStudy: any;
  constructor() { }

  ngOnInit(): void {
  }

}
