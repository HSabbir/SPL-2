import { TestBed } from '@angular/core/testing';

import { HigherstudyService } from './higherstudy.service';

describe('HigherstudyService', () => {
  let service: HigherstudyService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(HigherstudyService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
