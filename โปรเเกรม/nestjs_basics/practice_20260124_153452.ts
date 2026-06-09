// Session: Reviewing docs before bed
// Note: Need to memorize this syntax.

import { Module } from '@nestjs/common';
import { CatsController } from './cats.controller';
import { CatsService } from './cats.service';

// Source: NestJS Official Documentation - Modules
@Module({
  controllers: [CatsController],
  providers: [CatsService],
})
export class CatsModule {}