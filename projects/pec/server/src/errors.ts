export class AppError extends Error {
  status: number
  code: string
  details: unknown

  constructor(status: number, code: string, message: string, details?: unknown) {
    super(message)
    this.status = status
    this.code = code
    this.details = details ?? null
  }
}

export const badRequest = (msg: string, details?: unknown) => new AppError(400, 'BAD_REQUEST', msg, details)
export const unauthorized = (msg = 'authentication required') => new AppError(401, 'UNAUTHORIZED', msg)
export const forbidden = (msg: string) => new AppError(403, 'FORBIDDEN', msg)
export const notFound = (what: string) => new AppError(404, 'NOT_FOUND', `${what} not found`)
export const versionConflict = (details: unknown) =>
  new AppError(409, 'VERSION_CONFLICT', 'the record changed since you read it (PEC-NFR-004)', details)
export const conditionsOpen = (details: unknown) =>
  new AppError(409, 'CONDITIONS_OPEN', 'transition blocked by open hard conditions or active holds (I-5)', details)
