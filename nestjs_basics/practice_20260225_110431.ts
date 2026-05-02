// Session: Reviewing docs before bed
// Note: This took a while to debug, but it works now.

import { Module } from '@nestjs/common';
import { CatsController } from './cats.controller';
import { CatsService } from './cats.service';

// Source: NestJS Official Documentation - Modules
@Module({
  controllers: [CatsController],
  providers: [CatsService],
})
export class CatsModule {}