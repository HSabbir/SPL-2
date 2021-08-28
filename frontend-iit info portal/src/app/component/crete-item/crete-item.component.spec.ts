import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CreteItemComponent } from './crete-item.component';

describe('CreteItemComponent', () => {
  let component: CreteItemComponent;
  let fixture: ComponentFixture<CreteItemComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CreteItemComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(CreteItemComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
