import {Component, Input, OnInit} from '@angular/core';

@Component({
  selector: 'app-profession-cards',
  templateUrl: './profession-cards.component.html',
  styleUrls: ['./profession-cards.component.scss']
})
export class ProfessionCardsComponent implements OnInit {
  @Input()profession: any;
  constructor() { }

  ngOnInit(): void {
  }

}
