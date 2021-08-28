import {Component, Input, OnInit} from '@angular/core';

@Component({
  selector: 'app-research-card',
  templateUrl: './research-card.component.html',
  styleUrls: ['./research-card.component.scss']
})
export class ResearchCardComponent implements OnInit {
  @Input()research: any;
  constructor() { }

  ngOnInit(): void {
  }

}
