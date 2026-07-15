# Attempt 2 mechanical verifier defect

The rebuilt helper stopped before member execution because the existing owned
`members/DEL-12-01` evidence directory was not accepted by `Path.mkdir`.
Candidate and project writes were zero. The mechanical correction was to set
`exist_ok=True` for owned member evidence directories before full rerun.
