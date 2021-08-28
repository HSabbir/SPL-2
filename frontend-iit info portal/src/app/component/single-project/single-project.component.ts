import {Component, EventEmitter, Input, OnInit, Output} from '@angular/core';


@Component({
  selector: 'app-single-project',
  templateUrl: './single-project.component.html',
  styleUrls: ['./single-project.component.scss']
})
export class SingleProjectComponent implements OnInit {
  @Input()project: any;
  @Output() tag = new EventEmitter<string>();
  constructor() { }

  ngOnInit(): void {
  }
  tagEmit(str: string): void{
    this.tag.emit(str);
  }
}
